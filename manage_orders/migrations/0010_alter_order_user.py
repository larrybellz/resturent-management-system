# Generated by Django 4.1 on 2024-06-19 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0003_alter_clientuser_groups_and_more'),
        ('manage_orders', '0009_alter_orderitem_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authenticate.clientuser'),
        ),
    ]