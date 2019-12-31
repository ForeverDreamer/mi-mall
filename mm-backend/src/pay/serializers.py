from rest_framework import serializers

from .models import Wechat


class WechatCallbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wechat
        fields = [
            'status',
            'order_no',
        ]
