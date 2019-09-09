from django.db import models


# Create your models here.
class LoginUser(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=32, null=True, blank=True)
    age = models.IntegerField(default=23)

    username = models.CharField(max_length=32,null=True,blank=True)
    phone_num = models.CharField(max_length=11,null=True,blank=True)
    address = models.TextField()
    photo = models.ImageField(upload_to='image')
    gender = models.CharField(max_length=10,null=True,blank=True)


class Goods(models.Model):
    goods_num = models.CharField(max_length=11)
    goods_name = models.CharField(max_length=128)
    goods_price = models.FloatField()
    goods_count = models.IntegerField()
    goods_location = models.CharField(max_length=254)
    goods_pro_date = models.DateField(auto_now=True)
    goods_save_month = models.IntegerField()
    goods_status = models.IntegerField(default=1) # 1 上架，0 下架



