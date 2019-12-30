from django.urls import path

from .views import (
    ProductCartItemListView,
    ProductCartItemCreateView,
    ProductSkuListView,
    ProductCartItemUpdateView,
    ProductCartItemMutiDeleteView,
    ProductCartItemSingleDeleteView,
    )

urlpatterns = [
    path('', ProductCartItemListView.as_view(), name='cart-list'),
    path('add/', ProductCartItemCreateView.as_view(), name='cart-add'),
    path('skus/', ProductSkuListView.as_view(), name='cart-skus'),
    path('update/<str:pk>/', ProductCartItemUpdateView.as_view(), name='cart-update'),
    path('delete/', ProductCartItemMutiDeleteView.as_view(), name='cart-mutidelete'),
    path('delete/<str:pk>/', ProductCartItemSingleDeleteView.as_view(), name='cart-singledelete'),
]
