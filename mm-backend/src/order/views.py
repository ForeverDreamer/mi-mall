from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

from rest_framework import generics

from mm.exceptions import ParameterError
from .models import ShippingAddress, Coupon
from .serializers import (
    ShippingAddressListCreateSerializer,
    ShippingAddressUpdateSerializer,
    CouponListSerializer,
    ReceiveCouponCreateSerializer,
    ReceiveCouponListSerializer,
    OrderCreateSerializer,
)

User = get_user_model()


class ShippingAddressListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressListCreateSerializer


class ShippingAddressUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressUpdateSerializer


class CouponListAPIView(generics.ListAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponListSerializer


class CouponReceiveAPIView(generics.CreateAPIView):
    serializer_class = ReceiveCouponCreateSerializer

    def perform_create(self, serializer):
        owner = serializer.validated_data.get('owner')
        coupon = serializer.validated_data.get('coupon')
        coupon_list = owner.receivecoupon_set.all()
        for c in coupon_list:
            if coupon == c.coupon:
                raise ParameterError(detail="优惠券id:{}领取数量已达上限".format(coupon.id))
        serializer.save()


class CouponReceiveListAPIView(generics.ListAPIView):
    serializer_class = ReceiveCouponListSerializer

    def get_queryset(self):
        admin = User.objects.all().first()
        qs = admin.receivecoupon_set.all()
        return qs


class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer

    def perform_create(self, serializer):
        admin = User.objects.all().first()
        # 用户是否领取该优惠券,且没有使用
        coupon = serializer.validated_data.get('coupon')
        coupon_list = admin.receivecoupon_set.all()
        received = False
        coupon_received = None
        for c in coupon_list:
            if coupon == c.coupon:
                if c.used:
                    raise ParameterError(detail="该优惠券id:{}已经使用过".format(coupon.id))
                coupon_received = c
                received = True
        if not received:
            raise ParameterError(detail="用户没有领取过该优惠券id:{}".format(coupon.id))
        try:
            serializer.save(owner=admin, products_price=0, transport_costs=0)
            # 优惠券设置为已使用
            coupon_received.used = True
            coupon_received.save()
        except IntegrityError:
            raise ParameterError(detail='列表中某些商品不存在')
