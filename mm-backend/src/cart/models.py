from django.db import models
from django.contrib.auth import get_user_model

from product.models import Sku

User = get_user_model()

PRODUCT_COLOR = (
    ('re', '家'),
    ('company', '公司'),
    ('school', '学校'),
)

# 改变model结构时不能乱删migrations里边的文件，makemigrations时遇到非null字段需要设置默认值的，先将字段null=True，
# migrate成功，处理null字段数据之后，再改回来重新makemigrations和migrate


class CartQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(is_active=True)


class CartManager(models.Manager):
    def get_queryset(self):
        return CartQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()


# 购物车
class Cart(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    class Meta:
        verbose_name = '用户的购物车'
        verbose_name_plural = '用户的购物车'

    def __str__(self):
        return 'cart_{}'.format(self.owner.username)


# 购买商品和数量
class ProductCartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    sku = models.ForeignKey(Sku, on_delete=models.CASCADE)
    purchase_num = models.PositiveIntegerField()
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['cart', 'sku']
        verbose_name = '加入的购物车商品'
        verbose_name_plural = '加入的购物车商品'

    def __str__(self):
        return '{}_{}_{}'.format(self.sku.product.title, self.sku.version, self.sku.color)

