# -*- coding:utf-8 -*-


from django.shortcuts import render
from fangyuan.db import DB
import json
import re


def get_info(request):
    return render(request, 'info.html')


def index(request):
    return render(request, 'index.html')


def show_ditu(request):
    info = request.POST
    # print(request.POST)
    price1 = int(info['price1'])
    price2 = int(info['price2'])
    work_location = info['work-location']
    zuping = info['zuping']
    if zuping == 'HEZU':
        zuping = '合租'
    elif zuping == 'ZHENGZU':
        zuping = '整租'
    else:
        zuping = ''

    fangyuan = info['fangyuan']
    if fangyuan == 'GEREN':
        fangyuan = '个人'
    elif fangyuan == 'JINGJIREN':
        fangyuan = '经纪人'
    else:
        fangyuan = ''
    # jiaotong = info['jiaotong']
    print(work_location)
    print(price1)
    print(price2)
    print(zuping)
    print(fangyuan)
    # print(jiaotong)
    db = DB()
    house_info = db.select()
    mark_address = []
    mark_url = []
    temp = 0
    for i in house_info:
        house_title = i[1]
        house_url = i[2]
        try:
            house_price = int(i[3])
        except:
            house_price = 0
        house_zuping = i[4]
        house_size = i[5]
        house_xiaoqu = i[6]
        house_area = i[7]
        house_detailed_address = i[8]
        house_phone = i[9]
        house_man = i[10]
        temp += 1  # 记录数据库中的第几条数据
        if price1 <= house_price <= price2:
            if re.match(zuping, house_zuping) is not None:
                if re.search(fangyuan,house_man) is not None:
                    mark_address.append(house_detailed_address)
                    mark_url.append(house_url)
                    print(str(temp)+'success')
                else:
                    print(str(temp)+house_man)
            else:
                print(str(temp)+house_zuping)
        else:
            print(str(temp)+' '+str(house_price))
    print(temp)
    return render(request, 'ditu.html', {"workAddress": work_location,
                                         "markAddress": json.dumps(mark_address),
                                         "markUrl": json.dumps(mark_url)})
