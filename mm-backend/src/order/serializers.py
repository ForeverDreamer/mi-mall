from rest_framework import serializers

from .models import ShippingAddress, Coupon, ReceiveCoupon, Order


class ShippingAddressListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = [
            'id',
            'owner',
            'name',
            'cell_phone',
            'province',
            'county',
            'town',
            'street',
            'tag',
            'is_default',
        ]
        extra_kwargs = {'id': {'read_only': True}, 'owner': {'write_only': True}}


class ShippingAddressUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = [
            'id',
            'name',
            'cell_phone',
            'province',
            'county',
            'town',
            'street',
            'tag',
            'is_default',
        ]
        extra_kwargs = {'id': {'read_only': True}}


class CouponListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = [
            'id',
            'title',
            'desc',
            'discount_amount',
            'expense_amount',
            'limit_num',
            'start_time',
            'end_time',
        ]


class ReceiveCouponCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiveCoupon
        fields = [
            'id',
            'owner',
            'coupon',
        ]
        extra_kwargs = {'id': {'read_only': True}}


class ReceiveCouponListSerializer(serializers.ModelSerializer):
    coupon = CouponListSerializer(read_only=True)

    class Meta:
        model = ReceiveCoupon
        fields = [
            'coupon',
        ]


class OrderCreateSerializer(serializers.ModelSerializer):
    skus = serializers.ListField(child=serializers.IntegerField(), write_only=True)

    class Meta:
        model = Order
        fields = [
            'skus',
            'coupon',
            'shipping_address',
            'invoice',
        ]
        extra_kwargs = {'coupon': {'required': False}}
