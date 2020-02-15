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


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'cell_phone', 'province', 'county', 'town', 'street', 'tag', 'is_default',
                    'last_use_time', 'is_active', 'create_time', 'update_time')
    list_display_links = ('owner',)
    list_editable = ('name', 'cell_phone', 'province', 'county', 'town', 'street', 'tag', 'is_default', 'is_active')
    readonly_fields = ('owner',)

    class Meta:
        model = ShippingAddress


admin.site.register(ShippingAddress, ShippingAddressAdmin)


class CouponAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'discount_amount', 'expense_amount', 'limit_num', 'start_time', 'end_time',
                    'active', 'create_time', 'update_time')
    list_display_links = ('title',)
    # 'desc'字段太占空间，且不需要频繁修改，所以不加入list_editable
    list_editable = ('discount_amount', 'expense_amount', 'limit_num', 'start_time', 'end_time', 'active')

    class Meta:
        model = Coupon


admin.site.register(Coupon, CouponAdmin)


class ReceiveCouponAdmin(admin.ModelAdmin):
    list_display = ('owner', 'coupon', 'used', 'create_time', 'update_time')
    list_display_links = ('owner',)
    list_editable = ('coupon', 'used')

    class Meta:
        model = ReceiveCoupon


admin.site.register(ReceiveCoupon, ReceiveCouponAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_no', 'owner', 'coupon', 'products_price', 'transport_costs', 'shipping_address',
                    'invoice', 'status', 'pay_method', 'pay_time', 'pay_no', 'remark', 'active')
    list_display_links = ('order_no',)
    list_editable = ('transport_costs', 'shipping_address', 'invoice', 'remark', 'active')
    readonly_fields = ('order_no', 'owner', 'coupon', 'products_price', 'status', 'pay_method',
                       'pay_time', 'pay_no')

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'sku', 'purchase_num', 'sale_price', 'create_time', 'update_time')
    readonly_fields = ('order', 'sku', 'purchase_num', 'sale_price', 'create_time', 'update_time')

    class Meta:
        model = OrderItem


admin.site.register(OrderItem, OrderItemAdmin)


class OrderReviewAdmin(admin.ModelAdmin):
    list_display = ('order', 'comment', 'rating', 'active', 'create_time', 'update_time')
    list_display_links = ('order',)
    list_editable = ('active',)
    readonly_fields = ('order', 'comment', 'rating')

    class Meta:
        model = OrderReview


admin.site.register(OrderReview, OrderReviewAdmin)


class RefundAdmin(admin.ModelAdmin):
    list_display = ('refund_no', 'order', 'reason', 'status', 'active', 'create_time', 'update_time')
    list_display_links = ('refund_no',)
    list_editable = ('active',)
    readonly_fields = ('refund_no', 'order', 'reason', 'status')

    class Meta:
        model = Refund


admin.site.register(Refund, RefundAdmin)


class RefundReviewAdmin(admin.ModelAdmin):
    list_display = ('refund', 'comment', 'rating', 'active', 'create_time', 'update_time')
    list_display_links = ('refund',)
    list_editable = ('active',)
    readonly_fields = ('refund', 'comment', 'rating')

    class Meta:
        model = RefundReview


admin.site.register(RefundReview, RefundReviewAdmin)


class ShippingAdmin(admin.ModelAdmin):
    list_display = ('order', 'express_company', 'express_no', 'active', 'create_time', 'update_time')
    list_display_links = ('order',)
    list_editable = ('active',)
    readonly_fields = ('order', 'express_company', 'express_no')

    class Meta:
        model = Shipping


admin.site.register(Shipping, ShippingAdmin)


class ShippingReviewAdmin(admin.ModelAdmin):
    list_display = ('shipping', 'comment', 'rating', 'active', 'create_time', 'update_time')
    list_display_links = ('shipping',)
    list_editable = ('active',)
    readonly_fields = ('shipping', 'comment', 'rating')

    class Meta:
        model = ShippingReview


admin.site.register(ShippingReview, ShippingReviewAdmin)
