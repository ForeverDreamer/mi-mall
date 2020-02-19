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


# serializer_field没有传进来，文档是不是有误，或者新版本不支持此种方式？
# class CurrentCartDefault:
#     """
#     May be applied as a `default=...` value on a serializer field.
#     Returns the current user.
#     """
#     requires_context = True
#
#     def __call__(self, serializer_field):
#         return serializer_field.context['request'].user.cart
#

class CurrentCartDefault:
    def set_context(self, serializer_field):
        self.user = serializer_field.context['request'].user

    def __call__(self):
        return self.user.cart

    def __repr__(self):
        return '%s()' % self.__class__.__name__


class ProductCartItemCreateSerializer(serializers.ModelSerializer):
    cart = serializers.HiddenField(default=CurrentCartDefault())
    # def validate_cart(self, cart):
    #     user = self.context['request'].user
    #     if cart != user.cart:
    #         error_msg = "购物车id不匹配"
    #         logger.warning(user.username + ' => ' + error_msg)
    #         raise serializers.ValidationError(error_msg)
    #     return cart

    def validate_sku(self, sku):
        user = self.context['request'].user
        if sku.inventory < 1:
            error_msg = "库存不足"
            logger.warning(user.username + ' => ' + error_msg)
            raise serializers.ValidationError(error_msg)
        return sku

    class Meta:
        model = ProductCartItem
        fields = ['cart', 'sku', 'purchase_num']
        validators = [
            UniqueTogetherValidator(
                queryset=ProductCartItem.objects.all(),
                fields=['cart', 'sku']
            )]
        extra_kwargs = {
            # 'sku': {'error_messages': {'888666': '灭有库存'}},
            # 'purchase_num': {'write_only': True}
        }


class ProductCartItemMutiDeleteSerializer(serializers.Serializer):
    items = serializers.ListField(child=serializers.IntegerField())
