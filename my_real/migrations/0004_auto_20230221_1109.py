# Generated by Django 3.0.5 on 2023-02-21 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_real', '0003_auto_20230221_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='sqft',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
