from django.contrib import admin

from .models import ShippingAddress, Coupon, ReceiveCoupon, Order, OrderItem

admin.site.register(ShippingAddress)
admin.site.register(Coupon)
admin.site.register(ReceiveCoupon)
admin.site.register(Order)
admin.site.register(OrderItem)
