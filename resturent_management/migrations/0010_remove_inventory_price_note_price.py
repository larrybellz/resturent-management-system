# Generated by Django 4.1 on 2024-03-29 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturent_management', '0009_rename_date_added_note_date_updated_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='price',
        ),
        migrations.AddField(
            model_name='note',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]