# Generated by Django 2.2.1 on 2020-01-01 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20200101_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_no',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
