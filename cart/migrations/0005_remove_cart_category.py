# Generated by Django 4.2.3 on 2023-07-07 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_cart_category_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='category',
        ),
    ]
