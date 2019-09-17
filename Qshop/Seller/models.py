from django.db import models


# Create your models here.
class LoginUser(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=32, null=True, blank=True)
    age = models.IntegerField(default=23)

    username = models.CharField(max_length=32, null=True, blank=True)
    phone_num = models.CharField(max_length=11, null=True, blank=True)
    address = models.TextField()
    photo = models.ImageField(upload_to='seller/images')
    gender = models.CharField(max_length=10, null=True, blank=True)
    user_type = models.IntegerField(default=0)  # 0 买家，1商家，2管理员


class GoodsType(models.Model):
    type_name = models.CharField(max_length=32)
    type_desc = models.TextField()
    type_picture = models.ImageField(upload_to='seller/images',default='seller/images/banner01.jpg')
    """
        新鲜水果
        海鲜水产
        猪牛羊肉
        禽类蛋品
        新鲜蔬菜
        速冻食品
    """


class Goods(models.Model):
    goods_num = models.CharField(max_length=11)
    goods_name = models.CharField(max_length=128)
    goods_price = models.FloatField()
    goods_count = models.IntegerField()
    goods_location = models.CharField(max_length=254)
    goods_pro_date = models.DateField(auto_now=True)
    goods_save_month = models.IntegerField()
    goods_status = models.IntegerField(default=1)  # 1 上架，0 下架

    goods_picture = models.ImageField(upload_to='seller/images',default='seller/images/abc.jpg')
    goods_type = models.ForeignKey(to=GoodsType, on_delete=models.CASCADE,default=1)
    goods_store = models.ForeignKey(to=LoginUser, on_delete=models.CASCADE,default=1)

    goods_description = models.TextField(default="好吃不贵真正实惠，假一赔十")


class Valid_Code(models.Model):
    code_content = models.CharField(max_length=32)
    code_user = models.EmailField()
    code_time = models.DateTimeField(auto_now=True)
    code_state = models.IntegerField(default=0) # 0 未使用，1使用