from django.db import models


WECHAT_STATUS = (
    ('success', '付款成功'),
    ('fail', '付款失败'),
)


# 微信
class Wechat(models.Model):
    status = models.CharField(max_length=10, choices=WECHAT_STATUS)
    order_no = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Wechat'
        verbose_name_plural = 'Wechats'

    def __str__(self):
        return '{}_{}'.format(self.order_no, self.status)
