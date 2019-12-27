from django.urls import path

from .views import (
    ProductCartItemListView,
    ProductCartItemCreateView,
    )

urlpatterns = [
    path('', ProductCartItemListView.as_view(), name='cart-list'),
    path('add/', ProductCartItemCreateView.as_view(), name='cart-add'),
    # 修改购物车商品数量或型号(单个)
    path('update/', ProductCartItemCreateView.as_view(), name='cart-add'),
    # 删除购物车商品(单个或多个)
    path('delete/', ProductCartItemCreateView.as_view(), name='cart-add'),
]
