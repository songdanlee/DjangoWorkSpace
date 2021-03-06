# Generated by Django 2.1.8 on 2019-09-02 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0002_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(upload_to='images/img'),
        ),
    ]
