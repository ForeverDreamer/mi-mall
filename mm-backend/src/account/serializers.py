import logging

from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import serializers

from .validators import is_phone, is_veri_code, is_email, is_password

User = get_user_model()
LOGGER_NAME = '{}.{}'.format(settings.PROJECT_NAME, __name__)
logger = logging.getLogger(LOGGER_NAME)


class SendCodeSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=20)

    def validate_phone(self, phone):
        if not is_phone(phone):
            error_msg = "手机号格式错误"
            logger.warning(phone + ' => ' + error_msg)
            raise serializers.ValidationError(error_msg)
        return phone


class CodeRegOrLoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    veri_code = serializers.CharField()

    def validate_phone(self, phone):
        if not is_phone(phone):
            error_msg = "手机号格式错误"
            logger.warning(phone + ' => ' + error_msg)
            raise serializers.ValidationError(error_msg)
        return phone

    def validate_veri_code(self, veri_code):
        if not is_veri_code(veri_code):
            error_msg = "验证码格式错误"
            logger.warning(veri_code + ' => ' + error_msg)
            raise serializers.ValidationError(error_msg)
        return veri_code

    def create(self, validated_data):
        phone = validated_data.get('phone')
        # 创建用户
        user = User.objects.create_user(username=phone)
        # 创建用户信息
        # nickname = ''.join(['用户_', user.username])
        # Profile.objects.create(owner=user, nickname=nickname, mobile_phone=phone)
        return user


class AccountLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=20)

    def validate_username(self, username):
        if not (is_phone(username) or is_email(username)):
            error_msg = "电话号码或邮箱格式错误!"
            logger.warning(username + ' => ' + error_msg)
            raise serializers.ValidationError(error_msg)
        return username

    def validate_password(self, password):
        if not is_password(password):
            error_msg = "密码格式错误!"
            logger.warning(password + ' => ' + error_msg)
            raise serializers.ValidationError('密码格式错误！')
        return password
