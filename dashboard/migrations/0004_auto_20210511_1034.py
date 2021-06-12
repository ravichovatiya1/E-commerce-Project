# Generated by Django 3.2.1 on 2021-05-11 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0003_address_default_address_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='default_address_status',
            field=models.CharField(choices=[('true', 'true'), ('false', 'false')], default='false', max_length=20),
        ),
        migrations.CreateModel(
            name='DefaultAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dafault_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
