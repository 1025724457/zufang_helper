# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import time
from fangyuan_spider.items import FangyuanSpiderItem


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['sz.lianjia.com']
    start_urls = []
    base_url = 'http://sz.lianjia.com/zufang/pg'
    for i in range(1, 10):
        start_urls.append(base_url+str(i))
    url_num = 0
    parse_num = 0

    def parse(self, response):
        html = BeautifulSoup(response.body, 'lxml')
        house_list = html.select('.house-lst .info-panel h2 a')

        for a in house_list:
            url = a['href']
            self.url_num += 1
            yield scrapy.Request(url, callback=self.house_parse, dont_filter=True)

    def house_parse(self, response):

        print('时间：' + time.strftime('%H:%M:%S', time.localtime()))
        print('进入具体页面:')
        html = BeautifulSoup(response.body, 'lxml')
        house_url = response.url

        try:
            house_title = html.select('.title-wrapper .content .title .main')[0].get_text().strip().replace(u'\xa0', u' ')
            house_price = html.select('.overview .content .price .total')[0].get_text().strip().replace(u'\xa0', u' ')
            house_basic_info = html.select('.zf-content .zf-room p')
            house_size1 = house_basic_info[0].get_text('|').split('|')[1]
            house_size2 = house_basic_info[1].get_text('|').split('|')[1].split()
            if len(house_size2) > 1:
                house_zuping = house_size2[1]
            else:
                house_zuping = ''  # TODO 租凭为空

            house_size = house_size2[0] + '  ' +house_size1
            house_xiaoqu = house_basic_info[5].get_text('|').split('|')[1].split('\n')[0]
            house_area = house_basic_info[6].get_text('|').split('|')[1]
            house_detailed_address = house_xiaoqu
            house_phone = ''
            house_man = html.select('.overview .content .brokerInfo .brokerInfoText .brokerName .tag')[0].get_text()
            self.parse_num += 1

        except:
            print('页面解析错误')
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
        self.get_num()

        # print('房源URL：' + house_url)  # 房源url
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

    def get_num(self):
        print('总共url条数：'+str(self.url_num))
        print('解析页面数'+str(self.parse_num))






