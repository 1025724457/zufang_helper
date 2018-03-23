# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
from fangyuan.db import *


def url_spider(url):
    """
    爬取所有房源的链接
    """
    page = 0
    house_url_list = []  # 房源链接列表
    while True:
        page += 1
        # TODO 修改页码
        if page > 5:
            break
        page_url = url+'pn'+str(page)
        print(page_url)
        respones = requests.get(page_url)
        html = BeautifulSoup(respones.text, 'lxml')
        house_list = html.select('.des a[tongji_label]')  # 解析房源链接
        for a in house_list:
            temp = re.search('pinpaigongyu', str(a))  # 排除品牌公寓的房源链接
            if temp is None:
                house_url_list.append(a['href'])
        return house_url_list  # 返回房源链接列表


def house_spider(house_url_list):
    """
    爬取房源的详细信息
    """
    # house_url = ''  # 房源链接
    # house_price = ''  # 房源价格
    # house_title = ''  # 房源标题
    # house_zuping = ''  # 房源租凭方式
    # house_size = ''  # 房源类型大小 几室几厅 面积 装修
    # house_xiaoqu = ''  # 房源小区
    # house_area = ''  # 房源所属区域
    # house_detailed_address = ''  # 房源详细地址
    # house_phone = ''  # 电话
    # house_man = ''  # 联系人

    # TODO test create db
    if not exist_of_table('fangyuan_info'):
        print('table is not exist,create table...')
        create_table()
        print('create success')
    else:
        print('table exits')
    for house_url in house_url_list:
        respones = requests.get(house_url)
        html = BeautifulSoup(respones.text)
        try:
            house_title = html.select('.house-title h1')[0].get_text().strip()
            house_price = html.select('.f36')[0].get_text().strip()
            house_basic_info = html.select('.house-basic-info .f14 li span')
            house_zuping = house_basic_info[1].get_text().strip()
            house_size = house_basic_info[3].get_text().replace(' ', '')
            house_xiaoqu = house_basic_info[7].get_text().strip()
            # house_area = house_basic_info[9].get_text().replace('\n', '').replace(' ', '')
            house_area1 = house_basic_info[9].select('a')[0].get_text().replace('\n', '').replace(' ', '')
            house_area2 = house_basic_info[9].select('a')[1].get_text().replace('\n', '').replace(' ', '')
            house_area = house_area1 + '   ' + house_area2
            house_detailed_address = house_basic_info[11].get_text().strip()
            house_phone = html.select('.house-fraud-tip .house-chat-txt')[0].get_text()
            house_man = html.select('.house-agent-info .agent-name a')[0].get_text()
        except Exception as e:
            print('页面解析错误：'+house_url)
            print(e)
            continue

        print('房源URL：'+house_url)  # 房源url
        print('房源标题：'+house_title)  # 房源题目
        print('价格：'+house_price)  # 房源价格
        print('租凭方式：'+house_zuping)
        print('房源类型：'+house_size)
        print('所在小区：'+house_xiaoqu)
        print('所属区域：'+house_area)
        print('详细地址：'+house_detailed_address)
        print('联系电话：'+house_phone)
        print('联系人：'+house_man)
        print('\n')

        #存入数据库
        db = pymysql.connect(DB_IP, DB_USERNAME, DB_PASSWORD, TABLE, charset='utf8')
        cursor = db.cursor()
        insert(db=db, cursor=cursor, house_title=house_title, house_url=house_url, house_price=house_price,
               house_zuping=house_zuping, house_size=house_size, house_xiaoqu=house_xiaoqu, house_area=house_area,
               house_detailed_address=house_detailed_address, house_phone=house_phone, house_man=house_man)
        db.close()


if __name__ == '__main__':
    base_url = 'http://sz.58.com'
    url = 'http://sz.58.com/chuzu/'
    house_url_list = url_spider(url)
    house_spider(house_url_list)
