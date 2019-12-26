from django.db import models
from django.contrib.auth import get_user_model

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


class ShippingAddressQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


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
    tag = models.CharField(max_length=10, choices=ADDR_TAG)
    is_default = models.BooleanField(default=False)
    last_use_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    objects = ShippingAddressManager()

    def __str__(self):
        return '{}_{}_{}'.format(self.owner.username, self.name, self.tag)
