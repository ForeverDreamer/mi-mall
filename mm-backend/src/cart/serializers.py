import logging

from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from product.models import Sku
from .models import ProductCartItem

User = get_user_model()
LOGGER_NAME = '{}.{}'.format(settings.PROJECT_NAME, __name__)
logger = logging.getLogger(LOGGER_NAME)


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

    def validate_cart(self, cart):
        user = self.context['request'].user
        if cart != user.cart:
            error_msg = "购物车id不匹配"
            logger.warning(user.username + ' => ' + error_msg)
            raise serializers.ValidationError(error_msg)
        return cart

    class Meta:
        model = ProductCartItem
        fields = ['cart', 'sku', 'purchase_num']
        validators = [
            UniqueTogetherValidator(
                queryset=ProductCartItem.objects.all(),
                fields=['cart', 'sku']
            )]
        # extra_kwargs = {
        #     'sku': {'write_only': True},
        #     'purchase_num': {'write_only': True}
        # }


class ProductCartItemMutiDeleteSerializer(serializers.Serializer):
    items = serializers.ListField(child=serializers.IntegerField())
