# Generated by Django 4.1 on 2024-04-11 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resturent_management', '0015_category_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resturent_management.category'),
        ),
    ]
