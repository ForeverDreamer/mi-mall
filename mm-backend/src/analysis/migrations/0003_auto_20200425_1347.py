# Generated by Django 2.2.12 on 2020-04-25 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0002_config'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userloginlog',
            name='login_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userloginlog',
            name='login_type',
            field=models.CharField(choices=[('veri_code', '验证码登录'), ('account', '账户登录')], max_length=50),
        ),
    ]