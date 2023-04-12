# Generated by Django 4.1.2 on 2023-04-05 09:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0005_rename_product_baseproduct_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated At')),
                ('code', models.CharField(max_length=50, verbose_name='Code')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField(default=0, verbose_name='Sale Price')),
                ('start_time', models.DateField(blank=True, default=datetime.datetime(2023, 4, 5, 16, 33, 28, 545270), verbose_name='Start time')),
                ('end_time', models.DateField(blank=True, null=True, verbose_name='End Time')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='bill',
            name='sale_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sale_code_bill', to='shopapp.salecode'),
        ),
        migrations.AddField(
            model_name='historicalbill',
            name='sale_code',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='shopapp.salecode'),
        ),
    ]