# Generated by Django 4.2.3 on 2023-07-09 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_orders_customer'),
        ('cart', '0009_cart_order'),
    ]

    operations = [
        # migrations.AlterField(
        #     model_name='cart',
        #     name='order',
        #     field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.orders'),
        # ),
    ]
