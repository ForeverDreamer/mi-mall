from django.contrib import admin

from .models import Cart, ProductCartItem

admin.site.register(Cart)
admin.site.register(ProductCartItem)
