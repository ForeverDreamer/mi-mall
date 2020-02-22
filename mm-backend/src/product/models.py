import uuid

from django.db import models
from django.utils.html import format_html

from mm.utils import get_filename_ext

FIRST_CATEGORY = (
    ('recommends', '推荐'),
    ('cellphone', '手机'),
    ('Intelligence', '智能'),
    ('tv', '电视'),
    ('laptop', '笔记本'),
    ('appliance', '家电'),
    ('life', '生活周边'),
)

# SECOND_CATEGORY = (
#     ('xiao_mi', '小米'),
#     ('redmi', 'Redmi'),
#     ('price_range', '价位段'),
#     ('phone_new', '新品'),
#     ('5G', '5G专区'),
#     ('Intelligence_new', '爆款新品'),
#     ('redmi', 'Redmi'),
#     ('price_range', '价位段'),
#     ('phone_new', '新品'),
#     ('5G', '5G专区'),
# )

THEME_ACTIVITY = (
    ('new_arrival', '新品发布'),
    ('crowd_funding', '小米众筹'),
    ('hot', '热卖中'),
    ('old_for_new', '以旧换新'),
    ('seckill', '小米秒杀'),
    ('group_purchase', '一分拼团'),
)

ADPRODUCT_LOCATION = (
    # 注意不要有空格，否则会出现各种乱七八糟的问题
    ('carousel', '动态轮播图'),
    ('pos1', '位置1'),
    ('pos2', '位置2'),
    ('pos3', '位置3'),
    ('pos4', '位置4'),
)


class FirstCategoryQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


class FirstCategoryManager(models.Manager):
    def get_queryset(self):
        return FirstCategoryQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()


# 一级分类
class FirstCategory(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, choices=FIRST_CATEGORY)
    active = models.BooleanField(default=True)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    objects = FirstCategoryManager()

    def __str__(self):
        return self.title


class SecondCategoryQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


class SecondCategoryManager(models.Manager):
    def get_queryset(self):
        return SecondCategoryQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()


def second_category_image_upload(instance, filename):
    new_filename = uuid.uuid4()
    name, ext = get_filename_ext(filename)
    image_name = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "image/second_categor/{image_name}".format(image_name=image_name)


# 二级分类
class SecondCategory(models.Model):
    title = models.CharField(max_length=120)
    # slug = models.SlugField(unique=True, choices=SECOND_CATEGORY)
    first_category = models.ForeignKey(FirstCategory, on_delete=models.CASCADE)
    link_url = models.CharField(blank=True, max_length=50)
    img_height = models.IntegerField(blank=True)
    img_width = models.IntegerField(blank=True)
    cover_img = models.ImageField(upload_to=second_category_image_upload, height_field='img_height',
                                  width_field='img_width')
    order = models.IntegerField(default=1)
    active = models.BooleanField(default=True)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    objects = SecondCategoryManager()

    def __str__(self):
        return '{}_{}'.format(self.first_category.title, self.title)


class ThemeActivityQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


class ThemeActivityManager(models.Manager):
    def get_queryset(self):
        return ThemeActivityQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()


def theme_activity_image_upload(instance, filename):
    new_filename = uuid.uuid4()
    name, ext = get_filename_ext(filename)
    image_name = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "image/theme_activity/{image_name}".format(image_name=image_name)


# 主题活动
class ThemeActivity(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, choices=THEME_ACTIVITY)
    link_url = models.CharField(blank=True, max_length=50)
    img_height = models.IntegerField(blank=True)
    img_width = models.IntegerField(blank=True)
    cover_img = models.ImageField(upload_to=theme_activity_image_upload, height_field='img_height',
                                  width_field='img_width')
    order = models.IntegerField(default=1)
    active = models.BooleanField(default=True)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    objects = ThemeActivityManager()

    def __str__(self):
        return self.title


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(is_active=True)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def guess_you_like(self):
        product_list = self.all()
        recommend_list = []
        for p in product_list:
            for sku in p.sku_set.all().values('version', 'color', 'cover_img', 'original_price', 'discount_price'):
                recommend_list.append(sku)
        return recommend_list


def product_cover_image_upload(instance, filename):
    new_filename = uuid.uuid4()
    name, ext = get_filename_ext(filename)
    image_name = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "image/product/{product_id}/cover/{image_name}".format(product_id=instance.product.id, image_name=image_name)


# 产品
class Product(models.Model):
    title = models.CharField(max_length=120)
    desc = models.TextField()
    first_category = models.ForeignKey(FirstCategory, on_delete=models.CASCADE)
    second_category = models.ForeignKey(SecondCategory, on_delete=models.CASCADE)
    theme_activity = models.ForeignKey(ThemeActivity, null=True, blank=True, on_delete=models.SET_NULL)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    objects = ProductManager()

    def __str__(self):
        return self.title

    def short_desc(self):
        return format_html(
            '<span style="color: #{};">{}</span>',
            'FF0000',
            ''.join([self.desc[:5], ' ...'])
        )

    short_desc.short_description = 'short_desc'


def product_carousel_image_upload(instance, filename):
    new_filename = uuid.uuid4()
    name, ext = get_filename_ext(filename)
    image_name = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "image/product/{product_id}/carousel/{image_name}".format(product_id=instance.product.id, image_name=image_name)


class ProductCarouselImage(models.Model):
    product = models.ForeignKey(Product, related_name='carouse_images', on_delete=models.CASCADE)
    image_height = models.IntegerField(blank=True, null=True)
    image_width = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to=product_carousel_image_upload, height_field='image_height',
                              width_field='image_width')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.image)


# 产品规格
class Sku(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    version = models.CharField(max_length=50)
    color = models.CharField(max_length=10)
    img_height = models.IntegerField(blank=True)
    img_width = models.IntegerField(blank=True)
    cover_img = models.ImageField(upload_to=product_cover_image_upload, height_field='img_height',
                                  width_field='img_width')
    original_price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    discount_price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    inventory = models.PositiveIntegerField(default=9999)
    min_purchase_num = models.PositiveIntegerField(default=1)
    max_purchase_num = models.PositiveIntegerField(default=9999)
    is_active = models.BooleanField(default=True)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}_{}_{}'.format(self.product.title, self.version, self.color)


def product_detail_image_upload(instance, filename):
    new_filename = uuid.uuid4()
    name, ext = get_filename_ext(filename)
    image_name = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "image/product/detail/{product_id}/{image_name}".format(product_id=instance.product.id,
                                                                   image_name=image_name)


class ProductDetailImage(models.Model):
    product = models.ForeignKey(Product, related_name='detail_images', on_delete=models.CASCADE)
    img_height = models.IntegerField(blank=True, null=True)
    img_width = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to=product_detail_image_upload, height_field='image_height',
                              width_field='image_width')
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.image)


def ad_image_upload(instance, filename):
    new_filename = uuid.uuid4()
    name, ext = get_filename_ext(filename)
    image_name = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "image/ad/{location}/{image_name}".format(
        location=instance.location,
        image_name=image_name
    )


class AdProduct(models.Model):
    location = models.CharField(max_length=20, choices=ADPRODUCT_LOCATION)
    link_url = models.CharField(max_length=50)
    image_height = models.IntegerField(blank=True)
    image_width = models.IntegerField(blank=True)
    image = models.ImageField(upload_to=ad_image_upload, height_field='image_height',
                              width_field='image_width',
                              blank=True, null=True)

    class Meta:
        verbose_name = 'AdProduct'
        verbose_name_plural = 'AdProducts'

    def __str__(self):
        return self.location
