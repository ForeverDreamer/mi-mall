from django.contrib.auth import get_user_model

from rest_framework import serializers

from product.models import Sku
from .models import ProductCartItem

User = get_user_model()


class CartItemSkuDetailSerializer(serializers.ModelSerializer):
    product_id = serializers.CharField(source='product.id', read_only=True)
    product_title = serializers.CharField(source='product.title', read_only=True)

    class Meta:
        model = Sku
        fields = [
            'id',
            'product_id',
            'product_title',
            'version',
            'color',
            'cover_img',
            'original_price',
            'discount_price',
        ]


class ProductCartItemSerializer(serializers.ModelSerializer):
    sku = CartItemSkuDetailSerializer(read_only=True)

    class Meta:
        model = ProductCartItem
        fields = [
            'id',
            'sku',
            'purchase_num',
        ]
        read_only_fields = ['id']


class ProductCartItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCartItem
        fields = [
            'cart',
            'sku',
            'purchase_num',
        ]


class ProductCartItemMutiDeleteSerializer(serializers.Serializer):
    items = serializers.ListField(child=serializers.IntegerField())
