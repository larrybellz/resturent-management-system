# Generated by Django 4.1 on 2024-03-29 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resturent_management', '0002_remove_inventory_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='description',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='is_available',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='timeupdated',
        ),
    ]
