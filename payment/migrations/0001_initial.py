# Generated by Django 4.2.1 on 2023-06-21 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('payment_date_time', models.DateTimeField()),
                ('payment_status', models.BooleanField()),
                ('receipt', models.CharField(max_length=48)),
                ('payment_method', models.CharField(max_length=32)),
            ],
        ),
    ]