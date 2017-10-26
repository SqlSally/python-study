# 第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

#!/usr/bin/python3
import pymysql
def codeMysql():
    f = open('code200', 'r')
    conn = pymysql.connect(user='root', passwd='password')
    cursor = conn.cursor()
    cursor.execute('create database if not exists accode')
    cursor.execute('use accode')
    cursor.execute('create table accode(id int auto_increment primary key, code varchar(10))')
    for line in f.readlines():
        cursor.execute('insert into accode (code) values (%s)', [line.strip()])
    conn.commit()
    f.close()
    cursor.close()
    conn.close()




