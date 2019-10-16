# coding: utf-8
import psycopg2 as psycopg


def pg_demo():
    con = psycopg.connect(user='pgsql')
    cur = con.cursor()
    cur.execute('select * from pg_database')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    con.commit()
    con.close()
