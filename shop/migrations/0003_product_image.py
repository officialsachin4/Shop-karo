# Generated by Django 3.0.6 on 2020-05-26 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200526_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]
