# Generated by Django 4.1 on 2024-06-19 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resturent_management', '0020_menuitem_qauntity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='qauntity',
        ),
    ]
