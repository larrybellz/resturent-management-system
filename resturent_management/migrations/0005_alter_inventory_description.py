# Generated by Django 4.1 on 2024-03-29 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturent_management', '0004_inventory_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
