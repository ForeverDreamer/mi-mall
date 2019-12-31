from django.urls import path

from .views import (
    WechatAPIView,
    )

urlpatterns = [
    path('wechat/success/', WechatAPIView.as_view(), name='wechat-success'),
]
