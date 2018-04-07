# -*- coding:utf-8 -*-
import pymysql


DB_IP = 'localhost'
DB_USERNAME = 'root'
DB_PASSWORD = '123456'
TABLE = 'fangyuan'


class DB():

    def __init__(self):
        # 初始化连接数据库
        self.connect = pymysql.connect(DB_IP, DB_USERNAME, DB_PASSWORD, TABLE, charset='utf8')
        self.cursor = self.connect.cursor()

    def create_table(self):
        """
        创建数据库表
        :return:
        """
        create_table_sql = """CREATE TABLE fangyuan_info(
                    id int auto_increment primary key,
                    house_title varchar(100),
                    house_url varchar(500),
                    house_price varchar(10),
                    house_zuping varchar(20),
                    house_size varchar(30),
                    house_xiaoqu varchar(20),
                    house_area varchar(20),
                    house_detailed_address varchar(60),
                    house_phone varchar(20),
                    house_man varchar(20))default charset=utf8"""
        try:
            result = self.cursor.execute(create_table_sql)
            self.connect.commit()
            return result
        except:
            self.connect.rollback()

    def clear_table(self):
        try:
            result = self.cursor.execute('delete from fangyuan_info where 1=1')
            result2 = self.cursor.execute('truncate table fangyuan_info')
            self.connect.commit()
            return result, result2
        except Exception as e:
            print('delete fail')
            print(e)
            self.connect.rollback()

    def exist_of_table(self, table_name):
        """
        判断数据库中的表是否存在
        :param table_name:
        :return boolean:
        """
        self.cursor.execute('show tables')
        tables = self.cursor.fetchall()  # tables is tuple:(('fangyuan_info'))
        tables = list(tables)  # [('fangyuan_info')]
        for t in tables:
            # 将元组转换为列表 ['fangyuan_info']
            tables[tables.index(t)] = t[0]
        # print(tables)
        if table_name not in tables:
            # print('table not exist')
            return False
        else:
            # print('exist')
            return True

    def select(self):
        select_sql = """SELECT id,house_title,house_url,house_price,house_zuping,house_size,house_xiaoqu,house_area,
                        house_detailed_address,house_phone,house_man FROM fangyuan_info """

        try:
            self.cursor.execute(select_sql)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print('select failed')
            print(e)
        finally:
            self.close()

    def insert(self, house_title, house_url, house_price, house_zuping, house_size, house_xiaoqu, house_area,
               house_detailed_address, house_phone, house_man):
        """
        向数据库插入数据
        """
        insert_sql = """INSERT INTO fangyuan_info(house_title, house_url, house_price, house_zuping, house_size, 
                            house_xiaoqu, house_area, house_detailed_address, house_phone, house_man)
                            VALUES('{house_title}', '{house_url}', '{house_price}', '{house_zuping}', '{house_size}',
                            '{house_xiaoqu}', '{house_area}', '{house_detailed_address}', '{house_phone}', '{house_man}')"""
        insert_sql = insert_sql.format(house_title=house_title, house_url=house_url, house_price=house_price,
                                       house_zuping=house_zuping, house_size=house_size, house_xiaoqu=house_xiaoqu,
                                       house_area=house_area, house_detailed_address=house_detailed_address,
                                       house_phone=house_phone, house_man=house_man)
        try:
            result = self.cursor.execute(insert_sql)
            self.connect.commit()
            print('insert success\n')
            return result
        except Exception as e:
            self.connect.rollback()
            print('insert failed')
            print(e)

    def close(self):
        self.connect.close()


