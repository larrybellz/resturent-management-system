# Generated by Django 4.1 on 2024-06-19 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturent_management', '0021_remove_menuitem_qauntity'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='slug',
            field=models.SlugField(default='1'),
            preserve_default=False,
        ),
    ]