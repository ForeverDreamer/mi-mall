# Generated by Django 2.2.12 on 2020-04-27 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vue_admin', '0006_auto_20200426_1624'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admininfo',
            options={'verbose_name': '管理员信息', 'verbose_name_plural': '管理员信息'},
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': '导航目录', 'verbose_name_plural': '导航目录'},
        ),
        migrations.AlterField(
            model_name='menu',
            name='url',
            field=models.CharField(max_length=50),
        ),
    ]
