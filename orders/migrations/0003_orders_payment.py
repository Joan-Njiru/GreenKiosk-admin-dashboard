# Generated by Django 4.2.3 on 2023-07-07 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
        ('orders', '0002_alter_orders_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='payment',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='payment.payment'),
        ),
    ]
