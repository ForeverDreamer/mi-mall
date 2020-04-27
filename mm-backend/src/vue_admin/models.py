import uuid

from django.db import models
from django.contrib.auth import get_user_model

from mm.utils import get_filename_ext

User = get_user_model()


# 导航目录
# class NavMenu(models.Model):
#     owner = models.OneToOneField(User, on_delete=models.CASCADE)
#     active_index = models.PositiveIntegerField()
#     active = models.BooleanField(default=True)
#     create_time = models.DateTimeField(auto_now_add=True)
#     update_time = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name = 'NavMenu'
#         verbose_name_plural = 'NavMenus'
#
#     def __str__(self):
#         return self.owner.username


def avatar_upload(instance, filename):
    new_filename = uuid.uuid4()
    _, ext = get_filename_ext(filename)
    image_name = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "image/admin_info/{image_name}".format(image_name=image_name)


class AdminInfoQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def by_user(self, user):
        return self.filter(owner=user)


class AdminInfoManager(models.Manager):
    def get_queryset(self):
        return AdminInfoQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def by_user(self, user):
        return self.all().by_user(user)


class AdminInfo(models.Model):
    # navMenu = models.OneToOneField(NavMenu, on_delete=models.CASCADE)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    # name = models.CharField(max_length=50)
    active_index = models.PositiveIntegerField()
    width = models.IntegerField(blank=True)
    height = models.IntegerField(blank=True)
    avatar = models.ImageField(upload_to=avatar_upload, width_field='width', height_field='height')
    active = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    objects = AdminInfoManager()

    class Meta:
        verbose_name = '管理员信息'
        verbose_name_plural = '管理员信息'

    def __str__(self):
        return self.owner.username

    @property
    def name(self):
        return self.owner.username


class MenuQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def by_user(self, user):
        pass


class MenuManager(models.Manager):
    def get_queryset(self):
        return MenuQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def by_user(self, user):
        return self.all().by_user(user)


class Menu(models.Model):
    # navMenu = models.ForeignKey(NavMenu, related_name='menus', on_delete=models.CASCADE)
    user_set = models.ManyToManyField(User, related_name='user_menus')
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=20)
    sub_active_index = models.PositiveIntegerField()
    # parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    objects = MenuManager()

    class Meta:
        verbose_name = '导航目录'
        verbose_name_plural = '导航目录'

    def __str__(self):
        return self.name


class SubmenuQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    # user_set__contain会报错，正确的用法是怎样的？
    # def by_user(self, user):
    #     return self.filter(user_set__contains=user)


class SubmenuManager(models.Manager):
    def get_queryset(self):
        return SubmenuQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()
    #
    # def by_user(self, user):
    #     return self.all().by_user(user)


class Submenu(models.Model):
    menu = models.ForeignKey(Menu, related_name='submenus', on_delete=models.CASCADE)
    user_set = models.ManyToManyField(User, related_name='user_submenus')
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=20)
    url = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Submenu'
        verbose_name_plural = 'Submenus'

    def __str__(self):
        return self.name
