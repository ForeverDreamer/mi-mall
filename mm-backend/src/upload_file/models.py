import uuid
import re

from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save, post_save

from mm.utils import get_filename_ext

User = get_user_model()

# upload_file_name = ''


def file_upload(instance, filename):
    # global upload_file_name
    # upload_file_name = filename
    # 不知道为什么，title就是不能修改，size和active都没有问题，难道是CharField的问题，TextField也不行，暂时只能用pre_save处理
    instance.title = filename
    # instance.active = False
    instance.size = instance.upload_file.size
    new_filename = uuid.uuid4()
    name, ext = get_filename_ext(filename)
    file_name = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return 'upload/{username}/{file_name}'.format(username=instance.owner.username, file_name=file_name)


class FileItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    upload_file = models.FileField(upload_to=file_upload)
    size = models.BigIntegerField()
    active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '用户上传的文件'
        verbose_name_plural = '用户上传的文件'

    def __str__(self):
        return self.title

    @property
    def kb_size(self):
        return '{}(kb)'.format(str(self.size // 1000))


def file_pre_upload_receiver(sender, instance, *args, **kwargs):
    pattern = re.compile(r'^upload/')
    # 区分是上传文件自动修改，还是用户直接编辑title字段修改
    uploading = not re.search(pattern, instance.upload_file.name)
    if uploading:
        instance.title = instance.upload_file.name


pre_save.connect(file_pre_upload_receiver, sender=FileItem)


# def file_post_upload_receiver(sender, instance, created, *args, **kwargs):
#     print(args)
#     print(kwargs)
#     print(instance)
#     if created:
#         pass
#
#
# post_save.connect(file_post_upload_receiver, sender=FileItem)
