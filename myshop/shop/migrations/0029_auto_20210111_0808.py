# Generated by Django 2.0.8 on 2021-01-11 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0028_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]