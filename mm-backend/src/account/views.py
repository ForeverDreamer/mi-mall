import logging

from django.core.cache import cache
from django.conf import settings
from django.contrib.auth import get_user_model

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

User = get_user_model()

# LOGGER_NAME是'mm.account.views'
LOGGER_NAME = '{}.{}'.format(settings.PROJECT_NAME, __name__)
logger = logging.getLogger(LOGGER_NAME)


# 发送验证码
class SendCodeAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, *args, **kwargs):
        serializer = SendCodeSerializer(data=self.request.data)
        if not serializer.is_valid():
            error_msg = str(serializer.errors.get('phone')[0])
            logger.warning(error_msg)
            raise ParseError(detail=error_msg)
        data = serializer.validated_data
        phone = data.get('phone')
        # # 检查验证码缓存缓存
        # print('cache: [{}]-> {}'.format(mobile_phone, cache.get(mobile_phone)))
        if cache.get(phone):
            error_msg = '您操作太频繁，请稍后再试！'
            logger.warning(error_msg)
            raise ParseError(detail=error_msg)
        # 调用短信服务商接口发送验证码给用户
        cache.set(phone, '131452', 300)

        return Response({'msg': '发送成功'}, status=status.HTTP_200_OK)


class CodeRegOrLoginAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CodeRegOrLoginSerializer

    def create(self, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        if not serializer.is_valid():
            error_msg = serializer.errors
            logger.warning(error_msg)
            raise ParseError(detail=error_msg)
        data = serializer.validated_data
        phone = data.get('phone')
        # 缓存检查验证码是否一致
        # print('cache: [{}]-> {}'.format(mobile_phone, cache.get(mobile_phone)))
        if cache.get(phone) != data.get('veri_code'):
            error_msg = '验证码错误!'
            logger.warning(error_msg)
            raise PermissionDenied(detail=error_msg)

        qs = User.objects.filter(username=phone)
        if qs.exists():
            user = qs.first()
            # 用户是否被禁用
            if not user.is_active:
                error_msg = '用户被禁用!'
                logger.warning(error_msg)
                raise PermissionDenied(detail=error_msg)
            # 创建token返回给客户端
            # data = {'username': user.username, 'password': config.DEFALT_PASSWORD}
            # print('data', data)
            # token = requests.post(config.BASE_URL + '/api/token/', data=data).json()
            if self.request.user.is_authenticated:
                return Response({"msg": "token未过期无需更新"}, status=status.HTTP_200_OK)
            token = get_tokens_for_user(user)
            # print(token)
            # user.profile.logout = False
            # user.profile.save()
            return Response({"msg": "手机验证码登录成功", 'data': {'token': token}}, status=status.HTTP_200_OK)
        else:
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({"msg": "手机验证码注册成功", 'data': {'token': token}}, status=status.HTTP_201_CREATED)
