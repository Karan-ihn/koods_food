# Generated by Django 3.1 on 2020-08-14 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(default='food-item', max_length=100)),
                ('product_desc', models.CharField(default='food-item-description', max_length=500)),
                ('product_price', models.CharField(default='0', max_length=10)),
                ('date', models.DateField()),
            ],
        ),
    ]
