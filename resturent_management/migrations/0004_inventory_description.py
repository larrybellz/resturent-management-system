# Generated by Django 4.1 on 2024-03-29 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturent_management', '0003_remove_inventory_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]