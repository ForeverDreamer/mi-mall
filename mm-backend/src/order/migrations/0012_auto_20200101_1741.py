# Generated by Django 2.2.1 on 2020-01-01 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_auto_20200101_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_items',
            field=models.ManyToManyField(to='cart.ProductCartItem'),
        ),
    ]