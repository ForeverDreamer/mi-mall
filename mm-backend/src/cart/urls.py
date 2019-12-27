from django.urls import path

from .views import (
    ProductCartItemListView,
    ProductCartItemCreateView,
    )

urlpatterns = [
    path('', ProductCartItemListView.as_view(), name='cart-list'),
    path('add/', ProductCartItemCreateView.as_view(), name='cart-add'),
    # path('cellphone/', CellphoneAPIView.as_view(), name='cellphone'),
    # # 以下分类标签数据接口和手机几乎一样，暂时不用做
    # path('Intelligence//', RecommendsAPIView.as_view(), name='Intelligence'),
    # path('tv/', RecommendsAPIView.as_view(), name='tv'),
    # path('laptop//', RecommendsAPIView.as_view(), name='laptop'),
    # path('appliance/', RecommendsAPIView.as_view(), name='appliance'),
    # path('life/', RecommendsAPIView.as_view(), name='life'),
]
