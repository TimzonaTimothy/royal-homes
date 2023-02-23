# Generated by Django 3.0.5 on 2023-02-23 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_real', '0010_auto_20230222_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='property_type',
            field=models.CharField(blank=True, choices=[('Apartment', 'Apartment'), ('House', 'House'), ('Land', 'Land'), ('Others', 'Others')], max_length=255, null=True),
        ),
    ]