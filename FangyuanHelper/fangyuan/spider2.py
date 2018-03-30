import os
from fangyuan.db import DB


if __name__ == '__main__':
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
    os.system(r'scrapy crawl 58')
