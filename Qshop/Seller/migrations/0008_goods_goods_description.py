# Generated by Django 2.1.8 on 2019-09-10 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0007_goodstype_type_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='goods_description',
            field=models.TextField(default='好吃不贵真正实惠，假一赔十'),
        ),
    ]
