# Generated by Django 4.1 on 2024-03-29 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturent_management', '0006_remove_inventory_description_inventory_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
