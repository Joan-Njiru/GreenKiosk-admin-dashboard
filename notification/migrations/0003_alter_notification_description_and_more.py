# Generated by Django 4.2.3 on 2023-07-07 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_rename_time_and_date_notification_date_and_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='description',
            field=models.CharField(max_length=42),
        ),
        migrations.AlterField(
            model_name='notification',
            name='title',
            field=models.CharField(max_length=24),
        ),
    ]
