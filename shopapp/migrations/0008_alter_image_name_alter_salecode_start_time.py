# Generated by Django 4.1.2 on 2023-04-13 04:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0007_remove_comment_bill_order_comment_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='salecode',
            name='start_time',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 4, 13, 11, 25, 51, 984732), verbose_name='Start time'),
        ),
    ]
