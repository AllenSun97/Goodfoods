# Generated by Django 3.2.2 on 2021-08-23 03:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210823_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
