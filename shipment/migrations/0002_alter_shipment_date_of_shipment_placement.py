# Generated by Django 4.2.3 on 2023-07-07 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='date_of_shipment_placement',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
