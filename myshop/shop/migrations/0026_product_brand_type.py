# Generated by Django 2.0.8 on 2021-01-08 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_auto_20210108_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand_type',
            field=models.CharField(default='Local Brand', max_length=255),
        ),
    ]
