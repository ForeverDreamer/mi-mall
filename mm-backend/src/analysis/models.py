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
        verbose_name = 'Config'
        verbose_name_plural = 'Configs'


# 发送验证码日志
class SendCodeLog(models.Model):
    phone = models.CharField(max_length=20)
    veri_code = models.CharField(max_length=10)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'SendCodeLog'
        verbose_name_plural = 'SendCodeLogs'

    def __str__(self):
        return self.phone


# 用户登录日志
class UserLoginLog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    login_type = models.CharField(max_length=20, choices=LOGIN_TYPE)
    login_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'UserLoginLog'
        verbose_name_plural = 'UserLoginLogs'

    def __str__(self):
        return self.owner.username
