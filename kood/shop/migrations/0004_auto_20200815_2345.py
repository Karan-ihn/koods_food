# Generated by Django 3.1 on 2020-08-15 18:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200815_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_Json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField(max_length=12)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 15, 18, 15, 46, 793075, tzinfo=utc)),
        ),
    ]
