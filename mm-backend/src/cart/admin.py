from django.contrib import admin

from .models import Cart, ProductCartItem


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'is_active', 'create_time', 'update_time')
    list_display_links = ('owner',)
    readonly_fields = ('owner',)

    class Meta:
        model = Cart


admin.site.register(Cart, CartAdmin)


class ProductCartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'sku', 'purchase_num', 'create_time', 'update_time')
    list_display_links = ('cart',)
    list_editable = ('sku', 'purchase_num')
    readonly_fields = ('cart',)

    class Meta:
        model = ProductCartItem


admin.site.register(ProductCartItem, ProductCartItemAdmin)
