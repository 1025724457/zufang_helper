# -*- coding:utf-8 -*-

import pymysql


DB_IP = 'localhost'
DB_USERNAME = 'root'
DB_PASSWORD = 'sa'
TABLE = 'fangyuan'
def exist_of_table(table_name):
    """
    判断数据库中的表是否存在
    :param table_name:
    :return boolean:
    """
    db = pymysql.connect(DB_IP, DB_USERNAME, DB_PASSWORD, TABLE)
    cursor = db.cursor()
    cursor.execute('show tables')
    tables = cursor.fetchall()  # tables is tuple:(('fangyuan_info'))
    db.close()
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


def select():
    select_sql = """SELECT id,house_title,house_url,house_price,house_zuping,house_size,house_xiaoqu,house_area,
                    house_detailed_address,house_phone,house_man FROM fangyuan_info """
    db = pymysql.connect(DB_IP, DB_USERNAME, DB_PASSWORD, TABLE, charset='utf8')
    cursor = db.cursor()
    try:
        cursor.execute(select_sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print('select failed')
        print(e)
    finally:
        db.close()



def insert(db, cursor, house_title, house_url, house_price, house_zuping, house_size, house_xiaoqu, house_area,
           house_detailed_address, house_phone, house_man):
    """
    向数据库插入数据
    :param db:
    :param cursor:
    :param house_title:
    :param house_url:
    :param house_price:
    :param house_zuping:
    :param house_size:
    :param house_xiaoqu:
    :param house_area:
    :param house_detailed_address:
    :param house_phone:
    :param house_man:
    :return:
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
        result = cursor.execute(insert_sql)
        db.commit()
        print('insert success')
        return result
    except Exception as e:
        db.rollback()
        print('insert failed')
        print(e)


def create_table():
    """
    创建数据库表
    :return:
    """
    create_table_sql = """CREATE TABLE fangyuan(
                id int auto_increment primary key,
                house_title varchar(100),
                house_url varchar(500),
                house_price varchar(10),
                house_zuping varchar(20),
                house_size varchar(20),
                house_xiaoqu varchar(20),
                house_area varchar(20),
                hoouse_detailed_address varchar(60),
                house_phone varchar(20),
                house_man varchar(20))default charset=utf8"""
    db = pymysql.connect(DB_IP, DB_USERNAME, DB_PASSWORD, TABLE)
    cursor = db.cursor()
    try:
        result = cursor.execute(create_table_sql)
        db.commit()
        return result
    except:
        db.rollback()
    finally:
        db.close()


if __name__ == '__main__':
    # if not exist_of_table('fangyuan_info'):
    #     print('table is not exist,create table...')
    #     create_table()
    #     print('create success')
    # else:
    #     print('table exits')
    # db = pymysql.connect(DB_IP, DB_USERNAME, DB_PASSWORD, TABLE)
    # cursor = db.cursor()
    # insert(db=db, cursor=cursor, house_title='test1', house_url='test2', house_price='test3', house_zuping='test4',
    #        house_size='test5', house_xiaoqu='test6', house_area='test7', house_detailed_address='test8',
    #        house_phone='test9', house_man='test10')
    # db.close()
    info = select()
    for i in info:
        print(i)
