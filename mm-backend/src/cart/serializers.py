from rest_framework import serializers

from product.models import Sku
from .models import ProductCartItem


class CartItemSkuDetailSerializer(serializers.ModelSerializer):
    product_title = serializers.CharField(source='product.title', read_only=True)

    class Meta:
        model = Sku
        fields = [
            'product_title',
            'version',
            'color',
            'cover_img',
            'original_price',
            'discount_price',
        ]


class ProductCartItemListSerializer(serializers.ModelSerializer):
    sku = CartItemSkuDetailSerializer(read_only=True)

    class Meta:
        model = ProductCartItem
        fields = [
            'id',
            'sku',
            'purchase_num',
        ]


class ProductCartItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCartItem
        fields = [
            'sku',
            'purchase_num',
        ]
