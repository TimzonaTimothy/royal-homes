# Generated by Django 3.0.5 on 2023-02-21 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_real', '0004_auto_20230221_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='lot_size',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
    ]
