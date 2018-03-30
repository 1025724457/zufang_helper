# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from fangyuan_spider.db import DB


class FangyuanSpiderPipeline(object):
    def process_item(self, item, spider):
        db = DB()
        db.insert(item['title'], item['url'], item['price'], item['zuping'], item['size'], item['xiaoqu'], item['area'],
                  item['detailed_address'], item['phone'], item['host'])
        db.close()
        return item

    def init_db(self, db):
        if not db.exist_of_table('fangyuan_info'):
            print('数据库中表不存在，创建表中...')
            db.create_table()
        else:
            print('数据库中存在表，清除表数据...')
            db.clear_table()
            print('清除成功')


