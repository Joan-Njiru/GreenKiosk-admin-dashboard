# Generated by Django 4.2.3 on 2023-07-07 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_remove_cart_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default="2023-07-07T12:34:56"),
            preserve_default=False,
        ),
    ]