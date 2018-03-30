# -*- coding:utf-8 -*-
import csv
from fangyuan.db import DB


def to_excel():
    """将数据库中的数据导入到Excel表格"""
    db = DB()
    house_info = db.select()
    csv_file = open(r'D:\myproject\fangyuan_info.csv', 'w', newline='')
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(['house_title', 'house_url', 'house_price', 'house_zuping', 'house_size', 'house_xiaoqu',
                         'house_area', 'house_detailed_address', 'house_phone', 'house_man'])
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
        csv_writer.writerow([house_title, house_url, house_price, house_zuping, house_size, house_xiaoqu, house_area,
                             house_detailed_address, house_phone, house_man])
    csv_file.close()


if __name__ == '__main__':
    to_excel()
