# Generated by Django 2.0.8 on 2021-01-03 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20210103_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='https://pcbonlineshop.com/var/photo/product/2000x4000/4/176/4.jpg', upload_to='products/%Y/%m/%d'),
        ),
    ]
