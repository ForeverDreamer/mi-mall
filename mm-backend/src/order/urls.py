from django.urls import path

from .views import (
    ShippingAddressListCreateView,
    ShippingAddressUpdateDeleteView,
    )

urlpatterns = [
    path('shippingaddress/', ShippingAddressListCreateView.as_view(), name='shippingaddress-listcreate'),
    path('shippingaddress/<str:pk>/', ShippingAddressUpdateDeleteView.as_view(), name='shippingaddress-detail'),
    path('order/', ShippingAddressListCreateView.as_view(), name='order-listcreate'),
    # path('loadmore/', LoadMoreAPIView.as_view(), name='loadmore'),
    # path('cellphone/', CellphoneAPIView.as_view(), name='cellphone'),
    # # 以下分类标签数据接口和手机几乎一样，暂时不用做
    # path('Intelligence//', RecommendsAPIView.as_view(), name='Intelligence'),
    # path('tv/', RecommendsAPIView.as_view(), name='tv'),
    # path('laptop//', RecommendsAPIView.as_view(), name='laptop'),
    # path('appliance/', RecommendsAPIView.as_view(), name='appliance'),
    # path('life/', RecommendsAPIView.as_view(), name='life'),
]
