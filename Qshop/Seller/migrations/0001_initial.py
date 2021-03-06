# Generated by Django 2.1.8 on 2019-09-09 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_num', models.CharField(max_length=11)),
                ('goods_name', models.CharField(max_length=128)),
                ('goods_price', models.FloatField()),
                ('goods_count', models.IntegerField()),
                ('goods_location', models.CharField(max_length=254)),
                ('goods_pro_date', models.DateField(auto_now=True)),
                ('goods_save_month', models.IntegerField()),
                ('goods_status', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(blank=True, max_length=32, null=True)),
                ('age', models.IntegerField(default=23)),
                ('username', models.CharField(blank=True, max_length=32, null=True)),
                ('phone_num', models.CharField(blank=True, max_length=11, null=True)),
                ('address', models.TextField()),
                ('photo', models.ImageField(upload_to='image')),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
