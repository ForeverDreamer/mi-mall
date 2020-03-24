from django.urls import path

from .views import (
    SendCodeAPIView,
    AccountLoginAPIView,
    CodeRegOrLoginAPIView,
)


urlpatterns = [
    path('sendcode/', SendCodeAPIView.as_view(), name='sendcode'),
    path('coderegorlogin/', CodeRegOrLoginAPIView.as_view(), name='code_regorlogin'),
    path('passwordlogin/', AccountLoginAPIView.as_view(), name='password_login'),
]
