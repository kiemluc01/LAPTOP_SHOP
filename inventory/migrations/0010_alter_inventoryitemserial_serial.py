# Generated by Django 4.1.2 on 2023-04-15 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_alter_inventoryitemserial_serial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitemserial',
            name='serial',
            field=models.CharField(default=5076845828, max_length=50, verbose_name='Serial'),
        ),
    ]
