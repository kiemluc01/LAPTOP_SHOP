# Generated by Django 4.1.2 on 2023-03-18 15:18

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='District Name')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('addr_detail', models.CharField(max_length=250, verbose_name='Address Detail')),
                ('location', django.contrib.gis.db.models.fields.PointField(default='POINT(0 0)', srid=4326, verbose_name='Location')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(choices=[(0, 'step'), (1, 'confirmed')], verbose_name='State')),
                ('in_day', models.DateField(auto_now_add=True, verbose_name='day input')),
                ('confirmed_at', models.DateField(blank=True, null=True, verbose_name='confirmed At')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventoryIn', to='inventory.inventory')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(choices=[(0, 'step'), (1, 'confirmed')], verbose_name='State')),
                ('out_day', models.DateField(auto_now_add=True, verbose_name='day output')),
                ('confirmed_at', models.DateField(blank=True, null=True, verbose_name='confirmed At')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventoryOut', to='inventory.inventory')),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Provience Name')),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ward Name')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='district', to='inventory.district')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryOutItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name Item')),
                ('quantity', models.IntegerField(default=0, verbose_name='Amount')),
                ('inventory_in', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_out_item', to='inventory.inventoryout')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='Amount')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_item', to='inventory.inventory')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_item_product', to='shopapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryInItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name Item')),
                ('quantity', models.IntegerField(default=0, verbose_name='Amount')),
                ('inventory_in', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_in_item', to='inventory.inventoryin')),
            ],
        ),
        migrations.AddField(
            model_name='inventory',
            name='ward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ward', to='inventory.ward'),
        ),
        migrations.AddField(
            model_name='district',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='province', to='inventory.province'),
        ),
    ]