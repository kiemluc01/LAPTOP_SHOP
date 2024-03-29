# Generated by Django 4.1.2 on 2023-04-13 13:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0008_alter_image_name_alter_salecode_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_product', to='shopapp.baseproduct'),
        ),
        migrations.AlterField(
            model_name='salecode',
            name='start_time',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 4, 13, 20, 11, 2, 866719), verbose_name='Start time'),
        ),
    ]
