# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FangyuanSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 房源标题
    url = scrapy.Field()  # 房源连接
    price = scrapy.Field()  # 房源价格
    zuping = scrapy.Field()  # 房源租凭（整租/合租）
    size = scrapy.Field()  # 房源大小
    xiaoqu = scrapy.Field()  # 房源所在小区
    area = scrapy.Field()  # 房源所在地区
    detailed_address = scrapy.Field()  # 房源详细地址
    phone = scrapy.Field()  # 房东电话
    host = scrapy.Field()  # 房源联系人
