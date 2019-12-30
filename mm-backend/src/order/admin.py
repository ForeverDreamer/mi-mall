from django.contrib import admin

from .models import ShippingAddress, Coupon, ReceiveCoupon, Order

admin.site.register(ShippingAddress)
admin.site.register(Coupon)
admin.site.register(ReceiveCoupon)
admin.site.register(Order)
