from django.urls import path

from .views import (
    ShippingAddressListCreateAPIView,
    ShippingAddressUpdateDeleteAPIView,
    CouponListAPIView,
    CouponReceiveAPIView,
    CouponReceiveListAPIView,
    OrderCreateAPIView,
    OrderListAPIView,
    OrderCancelAPIView,
    OrderRefundAPIView,
    OrderConfirmReceiptAPIView,
    )

urlpatterns = [
    path('list/', OrderListAPIView.as_view(), name='list'),
    path('cancel/', OrderCancelAPIView.as_view(), name='cancel'),
    path('refund/', OrderRefundAPIView.as_view(), name='refund'),
    path('confirm/', OrderConfirmReceiptAPIView.as_view(), name='confirm'),
    path('shippingaddress/', ShippingAddressListCreateAPIView.as_view(), name='shippingaddress-listcreate'),
    path('shippingaddress/<str:pk>/', ShippingAddressUpdateDeleteAPIView.as_view(), name='shippingaddress-detail'),
    path('settlement/', OrderCreateAPIView.as_view(), name='settlement'),
    path('coupon/', CouponListAPIView.as_view(), name='coupon-list'),
    path('coupon/receive/', CouponReceiveAPIView.as_view(), name='coupon-receive'),
    path('coupon/receive/list/', CouponReceiveListAPIView.as_view(), name='coupon-receive-list'),
]
