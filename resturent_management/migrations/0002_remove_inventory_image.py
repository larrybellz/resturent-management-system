# Generated by Django 4.1 on 2024-03-29 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resturent_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='image',
        ),
    ]
