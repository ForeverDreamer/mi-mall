from rest_framework import generics

from .serializers import WechatCallbackSerializer


class WechatAPIView(generics.CreateAPIView):
    serializer_class = WechatCallbackSerializer

    def perform_create(self, serializer):
        serializer.save()
