# Generated by Django 2.1.8 on 2019-09-09 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginuser',
            name='user_type',
            field=models.IntegerField(default=0),
        ),
    ]
