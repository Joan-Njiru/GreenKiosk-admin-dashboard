# Generated by Django 4.2.3 on 2023-07-07 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_cart_timestamp'),
        ('orders', '0003_orders_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='customer_order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cart.cart'),
            preserve_default=False,
        ),
    ]
