# Generated by Django 2.0.8 on 2021-01-11 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0031_term'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
            ],
        ),
    ]