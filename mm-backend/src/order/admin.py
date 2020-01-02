from django.contrib import admin

from .models import (
    ShippingAddress,
    Coupon,
    ReceiveCoupon,
    Order,
    OrderItem,
    OrderReview,
    Refund,
    RefundReview,
    Shipping,
    ShippingReview
)

admin.site.register(ShippingAddress)
admin.site.register(Coupon)
admin.site.register(ReceiveCoupon)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderReview)
admin.site.register(Refund)
admin.site.register(RefundReview)
admin.site.register(Shipping)
admin.site.register(ShippingReview)
