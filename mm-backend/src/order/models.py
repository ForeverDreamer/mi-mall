from django.db import models
from django.contrib.auth import get_user_model

from product.models import Sku
from cart.models import ProductCartItem

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
    ('shipping', '待收货'),
    ('received', '待评价'),
    ('reviewed', '已评价'),
    ('refund', '退款'),
)

# SHIPPING_STATUS = (
#     ('pending', '打包中'),
#     ('shipped', '已发货'),
#     ('received', '已收货'),
# )

REFUND_STATUS = (
    ('applied', '申请退款'),
    ('processing', '退款中'),
    ('success', '退款成功'),
    ('fail', '退款失败'),
)

INVOICE_TYPE = (
    ('individual', '个人'),
    ('company', '公司'),
)

PAY_METHOD = (
    ('wechat', '微信'),
    ('alipay', '支付宝'),
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
        verbose_name = '收货地址'
        verbose_name_plural = '收货地址'

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
    limit_num = models.PositiveIntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    active = models.BooleanField(default=True)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    objects = CouponManager()

    class Meta:
        verbose_name = '优惠券'
        verbose_name_plural = '优惠券'

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
        verbose_name = '用户领取的优惠券'
        verbose_name_plural = '用户领取的优惠券'

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

    def by_id(self, order_id):
        return self.all().filter(id=order_id)


# 订单
class Order(models.Model):
    # 调用订单唯一流水号生成函数
    order_no = models.CharField(max_length=50, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # order_items = models.ManyToManyField(OrderItem)
    coupon = models.ForeignKey(Coupon, on_delete=models.PROTECT)
    # 商品总价
    products_price = models.DecimalField(decimal_places=2, max_digits=10)
    # 运输费用
    transport_costs = models.DecimalField(decimal_places=2, max_digits=10)
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.PROTECT)
    invoice = models.CharField(max_length=10, choices=INVOICE_TYPE)
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default=ORDER_STATUS[0][0])
    pay_method = models.CharField(max_length=10, blank=True, choices=PAY_METHOD)
    pay_time = models.DateTimeField(null=True, blank=True)
    pay_no = models.CharField(max_length=50, null=True, blank=True)
    remark = models.CharField(max_length=100, null=True, blank=True)  # 订单备注
    # 订单创建后一定时间内还未付款就关闭，恢复商品库存，优惠券等数据，使用定时任务
    # closed = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    objects = OrderManager()

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = '订单'

    def __str__(self):
        return '{}_{}'.format(self.owner.username, self.status)


# 购买商品和数量
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    sku = models.ForeignKey(Sku, on_delete=models.CASCADE)
    purchase_num = models.PositiveIntegerField()
    sale_price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '订单里的商品'
        verbose_name_plural = '订单里的商品'

    def __str__(self):
        return '{}_{}_{}_{}'.format(self.id, self.sku.product.title, self.sku.version, self.sku.color)


# 订单评价
class OrderReview(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.DecimalField(decimal_places=1, max_digits=1)
    active = models.BooleanField(default=True)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '订单评价'
        verbose_name_plural = '订单评价'


# 退款信息
class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    refund_no = models.CharField(max_length=50)
    reason = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=10, choices=REFUND_STATUS)
    active = models.BooleanField(default=True)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '退款信息'
        verbose_name_plural = '退款信息'

    def __str__(self):
        return '{}_{}'.format(self.refund_no, self.status)


# 退款评价
class RefundReview(models.Model):
    refund = models.ForeignKey(Refund, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.DecimalField(decimal_places=1, max_digits=1)
    active = models.BooleanField(default=True)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '退款评价'
        verbose_name_plural = '退款评价'


# 物流信息
class Shipping(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    express_company = models.CharField(max_length=20)
    # 第三方物流平台快递单号
    express_no = models.CharField(max_length=50)
    # status = models.CharField(max_length=10, choices=SHIPPING_STATUS)
    active = models.BooleanField(default=True)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '物流信息'
        verbose_name_plural = '物流信息'


# 物流评价
class ShippingReview(models.Model):
    shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.DecimalField(decimal_places=1, max_digits=1)
    active = models.BooleanField(default=True)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '物流评价'
        verbose_name_plural = '物流评价'
