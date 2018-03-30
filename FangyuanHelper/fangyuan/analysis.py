# -*- coding:utf-8 -*-
from fangyuan import db_old


def data_analysis():
    """根据数据库中的数据进行房源数据的分析"""
    house_info = db_old.select()
    for i in house_info:
        house_title = i[1]
        house_url = i[2]
        house_price = int(i[3])
        house_zuping = i[4]
        house_size = i[5]
        house_xiaoqu = i[6]
        house_area = i[7]
        house_detailed_address = i[8]
        house_phone = i[9]
        house_man = i[10]