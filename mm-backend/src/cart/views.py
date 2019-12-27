from rest_framework import generics

from .models import ProductCartItem
from .serializers import ProductCartItemListSerializer, ProductCartItemCreateSerializer
from .exceptions import InventoryShortage


# 获取购物车商品列表
class ProductCartItemListView(generics.ListAPIView):
    queryset = ProductCartItem.objects.all()
    serializer_class = ProductCartItemListSerializer


# 加入购物车
class ProductCartItemCreateView(generics.CreateAPIView):
    serializer_class = ProductCartItemCreateSerializer

    def perform_create(self, serializer):
        raise InventoryShortage()
        serializer.save()
