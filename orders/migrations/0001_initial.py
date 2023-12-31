# Generated by Django 4.2.1 on 2023-06-21 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=32)),
                ('placement_date_time', models.DateTimeField()),
                ('order_status', models.CharField(max_length=32)),
                ('no_of_orders', models.IntegerField()),
                ('total_order', models.IntegerField()),
            ],
        ),
    ]
