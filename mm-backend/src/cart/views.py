from django.contrib.auth import get_user_model

from rest_framework import generics

from .models import ProductCartItem, Sku
from .serializers import ProductCartItemListSerializer, ProductCartItemCreateSerializer
from .exceptions import InventoryShortage

User = get_user_model()


# 获取购物车商品列表
class ProductCartItemListView(generics.ListAPIView):
    queryset = ProductCartItem.objects.all()
    serializer_class = ProductCartItemListSerializer


# 加入购物车
class ProductCartItemCreateView(generics.CreateAPIView):
    serializer_class = ProductCartItemCreateSerializer

    def perform_create(self, serializer):
        sku = serializer.validated_data.get('sku')
        # 检测库存数量
        if sku.inventory < 1:
            raise InventoryShortage()
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
