# Generated by Django 3.0.5 on 2023-02-20 21:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.CharField(max_length=200)),
                ('listing_id', models.IntegerField()),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=300)),
                ('phone', models.IntegerField(blank=True)),
                ('message', models.TextField(blank=True)),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('zipcode', models.CharField(blank=True, max_length=20)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(blank=True, choices=[('Rent', 'Rent'), ('Sale', 'Sale'), ('Sole', 'Sold')], max_length=20, null=True)),
                ('price', models.IntegerField(blank=True)),
                ('bedrooms', models.IntegerField(blank=True)),
                ('bathrooms', models.DecimalField(blank=True, decimal_places=1, max_digits=2)),
                ('sqft', models.IntegerField(blank=True)),
                ('lot_size', models.DecimalField(blank=True, decimal_places=1, max_digits=5)),
                ('photo_main', models.ImageField(blank=True, upload_to='photos/%Y%m%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y%m%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y%m%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y%m%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y%m%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y%m%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y%m%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
