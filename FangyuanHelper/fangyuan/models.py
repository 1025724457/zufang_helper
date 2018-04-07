# -*- coding: UTF-8 -*-
from django.db import models


class HouseInfo(models.Model):
    title = models.CharField(max_length=100)  # 房源标题
    url = models.CharField(max_length=500)  # 房源连接
    price = models.CharField(max_length=10)  # 房源价格
    zuping = models.CharField(max_length=20)  # 房源租凭（整租/合租）
    size = models.CharField(max_length=30)  # 房源大小
    xiaoqu = models.CharField(max_length=20)  # 房源所在小区
    area = models.CharField(max_length=20)  # 房源所在地区
    detailed_address = models.CharField(max_length=60)  # 房源详细地址
    phone = models.CharField(max_length=20)  # 房东电话
    host = models.CharField(max_length=20)  # 房源联系人
