# Generated by Django 2.0.8 on 2020-12-30 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20201221_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cover/%Y/%m/%d')),
            ],
        ),
    ]
