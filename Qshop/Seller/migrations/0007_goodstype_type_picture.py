# Generated by Django 2.1.8 on 2019-09-09 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0006_auto_20190909_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodstype',
            name='type_picture',
            field=models.ImageField(default='seller/images/banner01.jpg', upload_to='seller/images'),
        ),
    ]
