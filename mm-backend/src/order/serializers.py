from rest_framework import serializers

from .models import (
    ShippingAddress,
    Coupon, ReceiveCoupon,
    Order,
    OrderItem,
    Refund,
)
from product.serializers import SkuListSerializer


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


class OrderItemSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    sku = SkuListSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = [
            'sku',
            'purchase_num',
            'sale_price',
            'total_price',
        ]

    def get_total_price(self, obj):
        return obj.sale_price * obj.purchase_num


class OrderListSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'order_no',
            'status',
            'order_items',
        ]


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'coupon',
            'shipping_address',
            'invoice',
        ]
        extra_kwargs = {'coupon': {'required': False}}


class OrderCancelSerializer(serializers.Serializer):
    order_id = serializers.IntegerField(min_value=1)


class OrderRefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refund
        fields = [
            'order',
            'reason',
        ]


class OrderConfirmReceiptSerializer(serializers.Serializer):
    order_id = serializers.IntegerField(min_value=1)
