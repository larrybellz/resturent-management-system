# Generated by Django 4.1 on 2024-04-20 12:35

from django.db import migrations, models
import django.utils.timezone
import resturent.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', resturent.models.UUIDField(editable=False, max_length=6, primary_key=True, serialize=False)),
                ('dish_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('order_state', models.BooleanField(default=False)),
            ],
        ),
    ]
