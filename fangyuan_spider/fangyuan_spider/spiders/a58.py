# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import re
import time
from  fangyuan_spider.items import FangyuanSpiderItem


global all_num
global su_num
global fail_num
global exec_list
all_num = 0
su_num = 0
fail_num = 0


class A58Spider(scrapy.Spider):
    name = '58'
    allowed_domains = ['sz.58.com/chuzu']
    start_urls = ['http://sz.58.com/chuzu']  # 抓取的页面
    num = 0

    def parse(self, response):
        global all_num
        html = BeautifulSoup(response.body, 'lxml')
        house_list = html.select('.des a[tongji_label]')  # 解析房源链接
        temp_num = 0
        res = []
        for a in house_list:
            temp = re.search('pinpaigongyu', str(a))  # 排除品牌公寓的房源链接
            if temp is None:
                url = a['href']
                temp_num += 1
                print('房源链接：'+str(temp_num)+' '+url)
                yield scrapy.Request(url, callback=self.house_parse, dont_filter=True)  # 回掉函数house_parse

    def house_parse(self, response):
        global su_num
        global fail_num
        global exce_list
        self.num += 1
        print('时间：'+time.strftime('%H:%M:%S', time.localtime()))
        print('进入具体页面:'+str(self.num))
        html = BeautifulSoup(response.body, 'lxml')
        house_url = response.url
        print('链接：'+house_url)
        try:
            house_title = html.select('.house-title h1')[0].get_text().strip().replace(u'\xa0', u' ')
            house_price = html.select('.f36')[0].get_text().strip().replace(u'\xa0', u' ')
            house_basic_info = html.select('.house-basic-info .f14 li span')
            house_zuping = house_basic_info[1].get_text().strip().replace(u'\xa0', u' ')
            house_size = house_basic_info[3].get_text().replace(' ', '').replace(u'\xa0', u' ')
            house_xiaoqu = house_basic_info[7].get_text().strip().replace(u'\xa0', u' ')
            house_area = house_basic_info[9].get_text().replace('\n', '').replace(' ', '').replace('\r', '').replace(
                u'\xa0', u' ')
            house_detailed_address = house_basic_info[11].get_text().strip().replace(u'\xa0', u' ')
            house_phone = html.select('.house-fraud-tip .house-chat-txt')[0].get_text().replace(u'\xa0', u' ')
            house_man = html.select('.house-agent-info .agent-name a')[0].get_text().replace(u'\xa0', u' ')
            su_num += 1
        except Exception as e:
            # exce_list.append(house_url)
            fail_num += 1
            print('页面解析错误：' )
            # print(traceback.format_exc())
            # print(html)
            return None

        item = FangyuanSpiderItem()
        item['title'] = house_title
        item['url'] = house_url
        item['price'] = house_price
        item['zuping'] = house_zuping
        item['size'] = house_size
        item['xiaoqu'] = house_xiaoqu
        item['area'] = house_area
        item['detailed_address'] = house_detailed_address
        item['phone'] = house_phone
        item['host'] = house_man

        yield item

        # # print('房源URL：' + house_url)  # 房源url
        # print('房源标题：' + house_title)  # 房源题目
        # print('价格：' + house_price)  # 房源价格
        # print('租凭方式：' + house_zuping)
        # print('房源类型：' + house_size)
        # print('所在小区：' + house_xiaoqu)
        # print('所属区域：' + house_area)
        # print('详细地址：' + house_detailed_address)
        # print('联系电话：' + house_phone)
        # print('联系人：' + house_man)
        # print('\n')



