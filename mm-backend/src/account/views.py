import logging

from django.core.cache import cache
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError, NotAuthenticated, AuthenticationFailed, PermissionDenied

from mm.exceptions import MyAuthenticationFailed, MyNotAuthenticated
from .serializers import (
    SendCodeSerializer,
    CodeRegOrLoginSerializer,
    AccountLoginSerializer,
)

from mm.exceptions import ParameterError
from .utils import get_tokens_for_user, is_login_too_often, admin_login
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
            raise PermissionDenied(detail=error_msg)
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
            raise NotAuthenticated(detail=error_msg)
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
            if is_login_too_often(user):
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


# 账号登录(手机/邮箱)
class AccountLoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, *args, **kwargs):
        serializer = AccountLoginSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        username = data.get('username')
        qs = User.objects.filter(username__exact=username)
        user = None
        if qs.exists():
            user = qs.first()
        else:
            qs = User.objects.filter(email__exact=username)
            if qs.exists():
                user = qs.first()
        if user:
            # 用户是否被禁用
            if not user.is_active:
                error_msg = '用户被禁用！'
                logger.warning(username + ' => ' + error_msg)
                raise PermissionDenied(detail=error_msg)
            # 比对密码，用户登录操作
            password = data.get('password')
            if not user.check_password(password):
                error_msg = '用户名或密码错误！'
                logger.warning(username + ' => ' + error_msg)
                raise MyAuthenticationFailed(detail=error_msg)
            # 创建token返回给客户端
            # headers = {'Content-Type': 'application/json'}
            # data = {'username': user.username, 'password': password}
            # # token = requests.post(config.BASE_URL+'/api/auth/token/', headers=headers, data=data)
            # token = requests.post(config.BASE_URL + '/api/auth/token/', data=data).json()
            if is_login_too_often(user):
                error_msg = '超过单日登录次数上限，禁用用户!'
                logger.warning(username + ' => ' + error_msg)
                raise PermissionDenied(detail=error_msg)
            token = get_tokens_for_user(user)
            # 该用户统计信息当日登录次数加1，防止消耗登录token攻击
            UserLoginLog.objects.create(owner=user, login_type=LOGIN_TYPE[1][0], login_name=username)
            nav_menu = admin_login(user)
            if nav_menu:
                data = {'token': token, 'navMenu': nav_menu}
            else:
                data = {'token': token}
            print(data)
            return Response({'msg': '账号登录成功', 'data': data}, status=status.HTTP_200_OK)
        else:
            error_msg = '用户名或密码错误!'
            logger.warning(username + ' => ' + error_msg)
            raise MyAuthenticationFailed(detail=error_msg)


# 邮箱登录，生成一个{uuid: email}的缓存，把链接发到用户邮箱，用户点击访问这个链接把uuid(token)进行验证，参考以下链接实现方式
# https://www.netsarang.com/en/downloading/?token=UjAwVEdwazlwREJvZWxMdFBodXVfUUBNTXBaaXdtT1RQYVJ3WHhrQ1F6RGdR
# https://login.linode.com/signup/E3E7E763-434B-4CD4-953CB2EAB5E07019
