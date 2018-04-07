import os
from fangyuan.db import DB
import time


if __name__ == '__main__':
    b_t = time.time()
    begin_time = time.strftime('%H:%M:%S', time.localtime(b_t))
    db = DB()
    # 如果数据库表不存在，则创建表
    if not db.exist_of_table('fangyuan_info'):
        print('table is not exist,create table...')
        db.create_table()
        print('create success')
    else:
        db.clear_table()  # 清除表数据
        print('table exits')
    db.close()
    os.chdir(r'D:\myproject\zufang_helper\fangyuan_spider')
    # os.system(r'scrapy crawl 58 --nolog')
    os.system(r'scrapy crawl 58 --nolog')
    os.system(r'scrapy crawl lianjia --nolog')
    e_t = time.time()
    end_time = time.strftime('%H:%M:%S', time.localtime(e_t))
    print('开始时间：'+begin_time)
    print('结束时间：'+end_time)
    process_time = (e_t - b_t)/60
    print('总时间：{0:.2f}'.format(process_time))
