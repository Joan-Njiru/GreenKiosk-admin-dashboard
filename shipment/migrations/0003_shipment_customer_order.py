# Generated by Django 4.2.3 on 2023-07-08 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_orders_customer'),
        ('shipment', '0002_alter_shipment_date_of_shipment_placement'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='customer_order',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='orders.orders'),
            preserve_default=False,
        ),
    ]
