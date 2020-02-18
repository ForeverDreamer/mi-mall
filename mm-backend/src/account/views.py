import logging

from django.core.cache import cache
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError, PermissionDenied

from .serializers import (
    SendCodeSerializer,
    CodeRegOrLoginSerializer
)

from mm.exceptions import ParameterError
from .utils import get_tokens_for_user
from analysis.models import Config, SendCodeLog, UserLoginLog, LOGIN_TYPE

User = get_user_model()

# LOGGER_NAME是'mm.account.views'
LOGGER_NAME = '{}.{}'.format(settings.PROJECT_NAME, __name__)
logger = logging.getLogger(LOGGER_NAME)


# 发送验证码
class SendCodeAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, *args, **kwargs):
        serializer = SendCodeSerializer(data=self.request.data)
        # if not serializer.is_valid():
        #     error_msg = str(serializer.errors.get('phone')[0])
        #     logger.warning(error_msg)
        #     raise ParseError(detail=error_msg)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        phone = data.get('phone')
        # # 检查验证码缓存缓存
        # print('cache: [{}]-> {}'.format(mobile_phone, cache.get(mobile_phone)))
        if cache.get(phone):
            error_msg = '您操作太频繁，请稍后再试！'
            logger.warning(phone + ' => ' + error_msg)
            raise ParseError(detail=error_msg)
        # 判断该手机号当日获取验证码次数是否超过警戒值，是则把手机号加入统计黑名单，返回错误信息，记录错误日志
        send_code_times_limit = Config.objects.first().send_code_times_limit
        today_times = SendCodeLog.objects.filter(create_time__date=timezone.now().date()).count()
        if today_times >= send_code_times_limit:
            error_msg = '超过单日验证码发送次数上限!'
            logger.warning(phone + ' => ' + error_msg)
            raise PermissionDenied(detail=error_msg)
        # 调用短信服务商接口发送验证码给用户
        veri_code = '131452'
        cache.set(phone, veri_code, 300)
        # 该手机号统计信息当日获取验证码次数加1，防止消耗验证码攻击
        SendCodeLog.objects.create(phone=phone, veri_code=veri_code)

        return Response({'msg': '发送成功'}, status=status.HTTP_200_OK)


class CodeRegOrLoginAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CodeRegOrLoginSerializer

    def create(self, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        # if not serializer.is_valid():
        #     error_msg = serializer.errors
        #     logger.warning(error_msg)
        #     raise ParseError(detail=error_msg)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        phone = data.get('phone')
        # 缓存检查验证码是否一致
        # print('cache: [{}]-> {}'.format(mobile_phone, cache.get(mobile_phone)))
        if cache.get(phone) != data.get('veri_code'):
            error_msg = '验证码错误!'
            logger.warning(phone + ' => ' + error_msg)
            raise PermissionDenied(detail=error_msg)
        # 清除验证码缓存
        cache.delete(phone)
        qs = User.objects.filter(username=phone)
        if qs.exists():
            user = qs.first()
            # 用户是否被禁用
            if not user.is_active:
                error_msg = '用户被禁用!'
                logger.warning(phone + ' => ' + error_msg)
                raise PermissionDenied(detail=error_msg)
            # 创建token返回给客户端
            # data = {'username': user.username, 'password': config.DEFALT_PASSWORD}
            # print('data', data)
            # token = requests.post(config.BASE_URL + '/api/token/', data=data).json()
            # if self.request.user.is_authenticated:
            #     error_msg = 'token未过期无需更新!'
            #     logger.warning(error_msg)
            #     raise ParseError(detail=error_msg)
            # 判断该用户当日登录次数是否超过警戒值，是则禁用该用户，返回错误信息，记录错误日志
            login_times_limit = Config.objects.first().login_times_limit
            today_times = UserLoginLog.objects.filter(create_time__date=timezone.now().date()).count()
            if today_times >= login_times_limit:
                user.is_active = False
                user.save()
                error_msg = '超过单日登录次数上限，禁用用户!'
                logger.warning(phone + ' => ' + error_msg)
                raise PermissionDenied(detail=error_msg)
            token = get_tokens_for_user(user)
            # 该用户统计信息当日登录次数加1，防止消耗登录token攻击
            UserLoginLog.objects.create(owner=user, login_type=LOGIN_TYPE[0][0], login_name=phone)
            # print(token)
            # user.profile.logout = False
            # user.profile.save()
            return Response({"msg": "手机验证码登录成功", 'data': {'token': token}}, status=status.HTTP_200_OK)
        else:
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({"msg": "手机验证码注册成功", 'data': {'token': token}}, status=status.HTTP_201_CREATED)
