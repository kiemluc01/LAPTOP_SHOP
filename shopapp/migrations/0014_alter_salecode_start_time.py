# Generated by Django 4.1.2 on 2023-04-17 13:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0013_alter_salecode_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salecode',
            name='start_time',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 4, 17, 20, 18, 1, 992048), verbose_name='Start time'),
        ),
    ]
