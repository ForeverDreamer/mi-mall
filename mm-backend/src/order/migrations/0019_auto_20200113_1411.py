# Generated by Django 2.2.1 on 2020-01-13 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0018_auto_20200102_1354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipping',
            old_name='shipping_no',
            new_name='express_no',
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='status',
        ),
        migrations.AddField(
            model_name='shipping',
            name='express_company',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
