#!/usr/bin/env python3
# coding=utf-8
import pymysql


class Mysql:
    def __init__(self, host, port, user, password, db=None, charset=None):
        self.conn = pymysql.connect(host, port, user, password, db, charset)
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def __enter__(self):
        """
        打开文件的方法打开数据库
        with DB() as f:
        :return:
        """
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cur.close()
        self.conn.close()
