from django.db import models
from django.contrib.auth import get_user_model

from product.models import Sku

User = get_user_model()

PRODUCT_COLOR = (
    ('re', '家'),
    ('company', '公司'),
    ('school', '学校'),
)


# 购买商品和数量
class ProductCartItem(models.Model):
    sku = models.ForeignKey(Sku, on_delete=models.CASCADE)
    purchase_num = models.IntegerField()
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)


class CartQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


class CartManager(models.Manager):
    def get_queryset(self):
        return CartQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()


# 购物车
class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductCartItem, blank=True)
    chosen_price = models.DecimalField(decimal_places=2, max_digits=10)
    is_active = models.BooleanField(default=True)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return '{}_{}_{}'.format(self.owner.username, self.name, self.tag)
