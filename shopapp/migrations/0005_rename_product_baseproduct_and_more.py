# Generated by Django 4.1.2 on 2023-04-04 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_remove_inventoryinitem_cpu_and_more'),
        ('chatbox', '0002_historychat_created_at_historychat_updated_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopapp', '0004_bill_billitem_cart_cartitem_historicalbill_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='BaseProduct',
        ),
        migrations.RenameModel(
            old_name='HistoricalProduct',
            new_name='HistoricalBaseProduct',
        ),
        migrations.AlterModelOptions(
            name='historicalbaseproduct',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical base product', 'verbose_name_plural': 'historical base products'},
        ),
        migrations.CreateModel(
            name='BillItemDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated At')),
                ('price', models.IntegerField(default=0, verbose_name='Price')),
                ('bill_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bill_item_detail', to='shopapp.billitem')),
                ('item_serial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bill_item_reial', to='inventory.inventoryitemserial')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
