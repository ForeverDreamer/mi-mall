from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

LOGIN_TYPE = (
    ('veri_code', '验证码登录'),
    ('account', '账户登录'),
)


# 配置
class Config(models.Model):
    send_code_times_limit = models.PositiveIntegerField()
    login_times_limit = models.PositiveIntegerField()

    class Meta:
        verbose_name = '配置'
        verbose_name_plural = '配置'


# 发送验证码日志
class SendCodeLog(models.Model):
    phone = models.CharField(max_length=20)
    veri_code = models.CharField(max_length=10)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '发送验证码日志'
        verbose_name_plural = '发送验证码日志'

    def __str__(self):
        return self.phone


# 用户登录日志
class UserLoginLog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    login_type = models.CharField(max_length=100, choices=LOGIN_TYPE)
    login_name = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '用户登录日志'
        verbose_name_plural = '用户登录日志'

    def __str__(self):
        return self.owner.username
