# Generated by Django 2.2.12 on 2020-04-27 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_auto_20200223_1257'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adproduct',
            options={'verbose_name': '广告推荐', 'verbose_name_plural': '广告推荐'},
        ),
        migrations.AlterModelOptions(
            name='firstcategory',
            options={'verbose_name': '一级分类', 'verbose_name_plural': '一级分类'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '商品', 'verbose_name_plural': '商品'},
        ),
        migrations.AlterModelOptions(
            name='secondcategory',
            options={'verbose_name': '二级分类', 'verbose_name_plural': '二级分类'},
        ),
        migrations.AlterModelOptions(
            name='themeactivity',
            options={'verbose_name': '主题活动', 'verbose_name_plural': '主题活动'},
        ),
    ]
