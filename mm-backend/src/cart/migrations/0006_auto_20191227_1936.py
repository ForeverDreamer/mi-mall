# Generated by Django 2.2.1 on 2019-12-27 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_remove_cart_chosen_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcartitem',
            name='sku',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.Sku'),
        ),
    ]