# -*- coding:utf-8 -*-

"""创建统计图"""
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


class Drawing(object):

    def __init__(self):
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    def create_pie(self, num, pie_name):

        """创建饼状图"""
        perc = num/num.sum()
        name = perc.index
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.pie(perc, labels=name, autopct='%1.1f%%')
        ax.axis('equal')
        ax.set_title(pie_name+'饼状图')
        # plt.show()

    def create_bar(self, num, bar_name):

        name = num.index
        fig = plt.figure()
        ax = fig.add_subplot(111)
        rect = ax.bar(name, num)
        ax.set_title(bar_name+'条形图')
        ax.set_ylabel('数量')
        # 在各条形图上添加标签
        for rec in rect:
            x = rec.get_x()
            height = rec.get_height()
            ax.text(x + 0.1, 1.02 * height, str(height))
        # plt.show()

    def create_hist(self, num, hist_name):
        """只适用于价格"""
        price = num
        price = pd.to_numeric(price, errors='coerce')  # str转换 num
        price = price[price < 20000]
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.hist(price, 100, range=(0, 20000))
        xmajorLocator = MultipleLocator(500)  # 将x主刻度标签设置为20的倍数
        # xmajorFormatter = FormatStrFormatter('%5.1f')  # 设置x轴标签文本的格式
        # xminorLocator = MultipleLocator(5)  # 将x轴次刻度标签设置为5的倍数

        ax.xaxis.set_major_locator(xmajorLocator)
        # ax.xaxis.set_major_formatter(xmajorFormatter)
        # ax.xaxis.set_minor_locator(xminorLocator)
        # ax.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
        ax.set_title(hist_name + '直方图')

    def show(self):
        plt.show()


class GetNum(object):
    """从Excel获取房源信息，进行简单处理"""
    def __init__(self):
        # 导入数据
        # self.header = ['house_title', 'house_url', 'house_price', 'house_zuping', 'house_size', 'house_xiaoqu',
        #                'house_area', 'house_detailed_address', 'house_phone', 'house_man']
        self.df = pd.read_csv(r'D:\myproject\fangyuan_info.csv', encoding='gbk')

    def get_area(self):
        area = self.df['house_area']
        area = area.replace(['南山区', '福田区', '宝安区', '盐田区', '罗湖区', '龙华.*', '坪山.*'],
                            ['南山', '福田', '宝安', '盐田', '罗湖', '龙华', '坪山'], regex=True)
        num = area.value_counts()  # 获取每个地区的数量
        return num

    def get_zuping(self):
        zuping = self.df['house_zuping']
        zuping = zuping.replace(['合租.*', '整租.*'], ['合租', '整租'], regex=True)
        zuping = zuping.fillna('空')
        num = zuping.value_counts()  # 获取每项的数量
        return num

    def get_price(self):
        price = self.df['house_price']
        return price

    def get_man(self):
        man = self.df['house_man']
        man = man.replace(['.*经纪人.*', '.*个人.*'], ['经纪人', '个人'], regex=True)
        num = man.value_counts()
        return num


def test_area():
    info = GetNum()
    drawing = Drawing()

    area_num = info.get_area()
    drawing.create_bar(area_num, '地区')
    drawing.create_pie(area_num, '地区')
    drawing.show()


def test_zuping():
    info = GetNum()
    drawing = Drawing()

    zuping_num = info.get_zuping()
    drawing.create_pie(zuping_num, '租凭')
    drawing.create_bar(zuping_num, '租凭')
    drawing.show()


def test_man():
    info = GetNum()
    drawing = Drawing()

    man_num = info.get_man()
    drawing.create_bar(man_num, '房主')
    drawing.create_pie(man_num, '房主')
    drawing.show()


def test_price():
    info = GetNum()
    drawing = Drawing()
    price = info.get_price()
    drawing.create_hist(price, '价格')
    drawing.show()


if __name__ == '__main__':
    # test_area()
    # test_zuping()
    # test_man()
    test_price()

