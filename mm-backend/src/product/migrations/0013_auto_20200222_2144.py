# Generated by Django 2.2.1 on 2020-02-22 13:44

from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20200213_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sku',
            name='inventory',
            field=models.PositiveIntegerField(default=9999),
        ),
        migrations.AlterField(
            model_name='sku',
            name='max_purchase_num',
            field=models.PositiveIntegerField(default=9999),
        ),
        migrations.AlterField(
            model_name='sku',
            name='min_purchase_num',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.CreateModel(
            name='ProductCarouselImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_height', models.IntegerField(blank=True, null=True)),
                ('image_width', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(height_field='image_height', upload_to=product.models.product_carousel_image_upload, width_field='image_width')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
        ),
    ]
