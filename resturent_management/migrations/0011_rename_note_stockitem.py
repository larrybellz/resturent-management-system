# Generated by Django 4.1 on 2024-03-29 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resturent_management', '0010_remove_inventory_price_note_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='note',
            new_name='StockItem',
        ),
    ]
