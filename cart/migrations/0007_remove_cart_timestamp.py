# Generated by Django 4.2.3 on 2023-07-07 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_cart_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='timestamp',
        ),
    ]