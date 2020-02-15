import logging

from django.conf import settings
from django.contrib.auth import get_user_model
# from django.core.exceptions import Do

from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response

from product.models import Product
from .models import ProductCartItem, Sku
from product.serializers import SkuListSerializer
from .serializers import (
    ProductCartItemSerializer,
    ProductCartItemCreateSerializer,
    ProductCartItemMutiDeleteSerializer,
)
from mm.exceptions import ParameterError
from .exceptions import InventoryShortage

User = get_user_model()
# LOGGER_NAME是'mm.cart.views'
LOGGER_NAME = '{}.{}'.format(settings.PROJECT_NAME, __name__)
logger = logging.getLogger(LOGGER_NAME)


# 获取购物车商品列表
class ProductCartItemListView(generics.ListAPIView):
    queryset = ProductCartItem.objects.all()
    serializer_class = ProductCartItemSerializer


# 加入购物车
class ProductCartItemCreateView(generics.CreateAPIView):
    serializer_class = ProductCartItemCreateSerializer

    def perform_create(self, serializer):
        sku = serializer.validated_data.get('sku')
        # 检测库存数量
        if sku.inventory < 1:
            error_msg = "库存不足"
            logger.warning(error_msg)
            raise ParameterError(detail=error_msg)
        # 已加入购物车则数量加1(不需要这么做，OneToOneField不允许重复创建，让客户端调用修改数量接口)
        # admin = User.objects.all().first()
        # cart_item = None
        # for item in admin.cart.items:
        #     if sku == item.sku:
        #         cart_item = item
        # if cart_item:
        #     cart_item.purchase_num += 1
        #     cart_item.save()
        # else:
        #     serializer.save()
        serializer.save()


# 获取单个产品的sku列表
class ProductSkuListView(generics.ListAPIView):
    serializer_class = SkuListSerializer

    def get_queryset(self):
        product_id = self.request.query_params.get('product_id')
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise NotFound()
        return product.sku_set.all()


# 修改购物车商品数量(单个)
class ProductCartItemUpdateView(generics.UpdateAPIView):
    serializer_class = ProductCartItemSerializer

    def get_queryset(self):
        admin = User.objects.all().first()
        qs = admin.cart.items.all()
        return qs


# 删除购物车商品(多个)
class ProductCartItemMutiDeleteView(APIView):
    def delete(self, *args, **kwargs):
        serializer = ProductCartItemMutiDeleteSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        items = serializer.validated_data.get('items')
        admin = User.objects.all().first()
        item_list = admin.cart.items.all()
        item_id_list = item_list.values_list('id')
        item_id_list = [item_id[0] for item_id in item_id_list]
        for item in items:
            if item not in item_id_list:
                error_msg = "商品id:{}不在购物车中".format(item)
                logger.warning(error_msg)
                raise ParameterError(detail=error_msg)
        for item in item_list:
            item.delete()
        return Response({"msg": "删除成功！"}, status=status.HTTP_200_OK)


# 删除购物车商品(单个)
class ProductCartItemSingleDeleteView(generics.DestroyAPIView):
    def get_queryset(self):
        admin = User.objects.all().first()
        qs = admin.cart.items.all()
        return qs
