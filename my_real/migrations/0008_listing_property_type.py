# Generated by Django 3.0.5 on 2023-02-21 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_real', '0007_auto_20230221_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='property_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
