import uuid

from django.db import models
from django.contrib.auth import get_user_model

from mm.utils import get_filename_ext

User = get_user_model()


# 导航目录
class NavMenu(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    active_index = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'NavMenu'
        verbose_name_plural = 'NavMenus'

    def __str__(self):
        return self.owner.username


def avatar_upload(instance, filename):
    new_filename = uuid.uuid4()
    _, ext = get_filename_ext(filename)
    image_name = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "image/admin_info/{image_name}".format(image_name=image_name)


class AdminInfo(models.Model):
    navMenu = models.OneToOneField(NavMenu, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    width = models.IntegerField(blank=True)
    height = models.IntegerField(blank=True)
    avatar = models.ImageField(upload_to=avatar_upload, width_field='width', height_field='height')
    active = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'AdminInfo'
        verbose_name_plural = 'AdminInfos'

    def __str__(self):
        return self.name


class Menu(models.Model):
    navMenu = models.ForeignKey(NavMenu, related_name='menus', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=20)
    sub_active_index = models.PositiveIntegerField()
    # parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        return self.name


class Submenu(models.Model):
    menu = models.ForeignKey(Menu, related_name='submenus', on_delete=models.CASCADE)
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
