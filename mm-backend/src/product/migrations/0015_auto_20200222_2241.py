# Generated by Django 2.2.1 on 2020-02-22 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_auto_20200222_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcarouselimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carouse_images', to='product.Product'),
        ),
    ]
