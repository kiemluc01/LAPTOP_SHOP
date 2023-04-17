# Generated by Django 4.1.2 on 2023-04-17 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0011_alter_cartitem_cart_alter_cartitem_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='quanlity',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='quantity'),
        ),
        migrations.AlterField(
            model_name='salecode',
            name='start_time',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 4, 17, 19, 30, 43, 453982), verbose_name='Start time'),
        ),
    ]
