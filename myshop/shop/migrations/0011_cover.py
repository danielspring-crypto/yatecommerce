# Generated by Django 2.0.8 on 2020-12-30 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20201230_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='coverimage/%Y/%m/%d')),
                ('text1', models.CharField(default='yate', max_length=255)),
                ('text2', models.CharField(default='yate', max_length=255)),
            ],
        ),
    ]