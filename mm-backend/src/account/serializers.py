from django.contrib.auth import get_user_model

from rest_framework import serializers

from .validators import is_phone, is_veri_code

User = get_user_model()


class SendCodeSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=20)

    def validate_phone(self, phone):
        if not is_phone(phone):
            raise serializers.ValidationError('手机号格式错误！')
        return phone


class CodeRegOrLoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    veri_code = serializers.CharField()

    def validate_phone(self, phone):
        if not is_phone(phone):
            raise serializers.ValidationError('手机号格式错误！')
        return phone

    def validate_veri_code(self, veri_code):
        if not is_veri_code(veri_code):
            raise serializers.ValidationError('验证码格式错误！')
        return veri_code

    def create(self, validated_data):
        phone = validated_data.get('phone')
        # 创建用户
        user = User.objects.create_user(username=phone)
        # 创建用户信息
        # nickname = ''.join(['用户_', user.username])
        # Profile.objects.create(owner=user, nickname=nickname, mobile_phone=phone)
        return user
