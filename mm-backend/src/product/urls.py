from django.urls import path

from .views import (
    RecommendsAPIView,
    LoadMoreAPIView,
    )

urlpatterns = [
    path('recommends/', RecommendsAPIView.as_view(), name='recommends'),
    path('recommends/loadmore/', LoadMoreAPIView.as_view(), name='recommends-loadmore'),
    path('cellphone/', RecommendsAPIView.as_view(), name='cellphone'),
    path('Intelligence/<str:slug>/', RecommendsAPIView.as_view(), name='Intelligence'),
    path('tv/', RecommendsAPIView.as_view(), name='tv'),
    path('laptop/<str:pk>/', RecommendsAPIView.as_view(), name='laptop'),
    path('appliance/', RecommendsAPIView.as_view(), name='appliance'),
    path('life/', RecommendsAPIView.as_view(), name='life'),
]
