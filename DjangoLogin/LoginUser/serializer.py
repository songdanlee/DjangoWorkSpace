from rest_framework import serializers
from LoginUser.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:  # 元类
        model = LoginUser
        fields = [
            "email",
            "password",
            "username",
            "phone_num",
            "address",
            "photo",
            "gender"
        ]  # 接口返回字段

class GoodsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Goods
        fields = [
            "goods_num",
            "goods_name",
            "goods_price",
            "goods_count",
            "goods_location",
            "goods_pro_date",
            "goods_save_month",
            "goods_status"
        ]
