# Generated by Django 3.2.1 on 2021-05-10 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_address_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='default_address_status',
            field=models.CharField(choices=[('true', 'true'), ('false', 'false')], default='true', max_length=20),
        ),
    ]