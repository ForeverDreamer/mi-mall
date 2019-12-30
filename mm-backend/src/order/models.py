from django.db import models
from django.contrib.auth import get_user_model

from product.models import Sku

User = get_user_model()

# PROVINCE = (
#     ('recommends', '推荐'),
#     ('cellphone', '手机'),
#     ('Intelligence', '智能'),
#     ('tv', '电视'),
#     ('laptop', '笔记本'),
#     ('appliance', '家电'),
#     ('life', '生活周边'),
# )
#
# COUNTY = (
#     ('recommends', '推荐'),
#     ('cellphone', '手机'),
#     ('Intelligence', '智能'),
#     ('tv', '电视'),
#     ('laptop', '笔记本'),
#     ('appliance', '家电'),
#     ('life', '生活周边'),
# )
#
# TOWN = (
#     ('recommends', '推荐'),
#     ('cellphone', '手机'),
#     ('Intelligence', '智能'),
#     ('tv', '电视'),
#     ('laptop', '笔记本'),
#     ('appliance', '家电'),
#     ('life', '生活周边'),
# )

ADDR_TAG = (
    ('home', '家'),
    ('company', '公司'),
    ('school', '学校'),
)

ORDER_STATUS = (
    ('unpaid', '待付款'),
    ('paid', '已付款'),
    ('shipped', '已发货'),
    ('received', '已收货'),
)

INVOICE_TYPE = (
    ('individual', '个人'),
    ('company', '公司'),
)


class ShippingAddressQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(is_active=True)


class ShippingAddressManager(models.Manager):
    def get_queryset(self):
        return ShippingAddressQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()


# 收货地址
class ShippingAddress(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    cell_phone = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    county = models.CharField(max_length=20)
    town = models.CharField(max_length=20)
    street = models.CharField(max_length=100)
    tag = models.CharField(max_length=10, choices=ADDR_TAG, null=True, blank=True)
    is_default = models.BooleanField(default=False)
    last_use_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    objects = ShippingAddressManager()

    class Meta:
        verbose_name = 'ShippingAddress'
        verbose_name_plural = 'ShippingAddresses'

    def __str__(self):
        return '{}_{}_{}'.format(self.owner.username, self.name, self.street)


class CouponQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


class CouponManager(models.Manager):
    def get_queryset(self):
        return CouponQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()


# 优惠券
class Coupon(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    # 抵扣金额
    discount_amount = models.DecimalField(decimal_places=2, max_digits=10)
    # 需要购满金额
    expense_amount = models.DecimalField(decimal_places=2, max_digits=10)
    # 每人限领数量
    limit_num = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    active = models.BooleanField(default=True)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    objects = CouponManager()

    class Meta:
        verbose_name = 'Coupon'
        verbose_name_plural = 'Coupons'

    def __str__(self):
        return self.title


# 优惠券领取信息
class ReceiveCoupon(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    used = models.BooleanField(default=False)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'ReceiveCoupon'
        verbose_name_plural = 'ReceiveCoupons'

    def __str__(self):
        return '{}_{}'.format(self.owner.username, self.coupon.title)


class OrderQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


class OrderManager(models.Manager):
    def get_queryset(self):
        return OrderQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()


# 订单
class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default=ORDER_STATUS[0][0])
    skus = models.ManyToManyField(Sku)
    coupon = models.ForeignKey(Coupon, on_delete=models.PROTECT)
    # 商品总价
    products_price = models.DecimalField(decimal_places=2, max_digits=10)
    # 运输费用
    transport_costs = models.DecimalField(decimal_places=2, max_digits=10)
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.PROTECT)
    invoice = models.CharField(max_length=10, choices=INVOICE_TYPE)
    active = models.BooleanField(default=True)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    objects = OrderManager()

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return '{}_{}'.format(self.owner.username, self.status)
