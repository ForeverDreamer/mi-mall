from django.urls import path

from .views import (
    SendCodeAPIView,
    CodeRegOrLoginAPIView,
)


urlpatterns = [
    path('sendcode/', SendCodeAPIView.as_view(), name='sendcode'),
    path('coderegorlogin/', CodeRegOrLoginAPIView.as_view(), name='code_regorlogin'),
]
