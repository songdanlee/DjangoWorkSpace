from django.db import models
from Seller.models import *
# Create your models here.


class PayOrder(models.Model):
    """
    订单表
        订单状态
        0 未支付
        1 已支付
        2 待发货
        3 待发货
        4/5 完成/拒收
    """
    order_number = models.CharField(max_length=32)
    order_date = models.DateTimeField(auto_now=True)
    order_status = models.IntegerField()
    order_total = models.FloatField(blank=True,null=True)
    order_user = models.ForeignKey(to=LoginUser,on_delete=models.CASCADE)
    goods_number = models.IntegerField(default=1)

class OrderInfo(models.Model):
    """
    订单详情
    """
    order_id = models.ForeignKey(to=PayOrder,on_delete=models.CASCADE)
    goods_id = models.IntegerField()
    goods_picture = models.CharField(max_length=32)
    goods_name = models.CharField(max_length=32)
    goods_count = models.IntegerField()
    goods_price = models.FloatField() # 单价
    goods_total_price = models.FloatField() # 小计
    store_id = models.ForeignKey(to=LoginUser,on_delete=models.CASCADE)

class Cart(models.Model):
    """
    商品名称
    商品数量
    商品价格
    商品图片
    商品总价
    商品id
    用户
    """
    goods_name = models.CharField(max_length=32)
    goods_num = models.IntegerField()
    goods_price = models.FloatField()
    goods_picture = models.CharField(max_length=32)
    goods_total = models.FloatField()
    goods_id = models.IntegerField()
    cart_user = models.IntegerField()

