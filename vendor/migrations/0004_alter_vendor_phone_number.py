# Generated by Django 4.2.4 on 2023-08-18 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_alter_vendor_password_alter_vendor_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]