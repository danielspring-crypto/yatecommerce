# Generated by Django 2.0.8 on 2021-01-04 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_delete_cover3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cover3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image3', models.ImageField(default='https://pcbonlineshop.com/var/photo/product/2000x4000/4/176/4.jpg', upload_to='covers/%Y/%m/%d')),
                ('text3', models.CharField(max_length=255)),
                ('body3', models.CharField(max_length=255)),
            ],
        ),
    ]
