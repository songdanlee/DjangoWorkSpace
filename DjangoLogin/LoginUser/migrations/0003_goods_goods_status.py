# Generated by Django 2.1.8 on 2019-09-05 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginUser', '0002_auto_20190905_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='goods_status',
            field=models.IntegerField(default=1),
        ),
    ]
