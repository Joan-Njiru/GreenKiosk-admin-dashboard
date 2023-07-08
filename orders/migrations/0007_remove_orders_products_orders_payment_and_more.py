# Generated by Django 4.2.3 on 2023-07-08 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
        ('orders', '0006_remove_orders_order_id_remove_orders_payment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='products',
        ),
        migrations.AddField(
            model_name='orders',
            name='payment',
            field=models.ManyToManyField(to='payment.payment'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_status',
            field=models.CharField(max_length=24),
        ),
    ]