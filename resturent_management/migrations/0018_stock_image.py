# Generated by Django 4.1 on 2024-05-08 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturent_management', '0017_delete_categ'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='dish_image/'),
        ),
    ]
