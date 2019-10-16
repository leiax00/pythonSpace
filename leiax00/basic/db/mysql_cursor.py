# coding: utf-8
import pymysql


def mysql_demo():
    con = pymysql.connect(user='pgsql')
    cur = con.cursor()
    cur.execute('select * from pg_database')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    con.commit()
    con.close()
