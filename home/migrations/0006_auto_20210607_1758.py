# Generated by Django 3.2.1 on 2021-06-07 12:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210607_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product_Upload_Date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 7, 17, 58, 49, 117534), null=True),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='Review_DateTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 7, 17, 58, 49, 117534)),
        ),
    ]