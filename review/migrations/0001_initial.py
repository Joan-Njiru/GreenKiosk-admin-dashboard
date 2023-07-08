# Generated by Django 4.2.3 on 2023-07-07 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=48)),
                ('time_and_date', models.DateTimeField()),
                ('sender_name', models.CharField(max_length=24)),
            ],
        ),
    ]
