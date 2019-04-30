#!/usr/bin/env python3

# @FileName : mysql_util.py
# @作者 : Liu
# @日期 : 2019年04月11日
# @时间 : 11时08分

import pymysql
from configparser import ConfigParser
import os


class mysql_util(object):
    def __init__(self, filenames=None):
        self.conf = ConfigParser()
        self.filenames = filenames
        self.conn = None
        self.cursor = None
        if self.filenames:
            # 配置文件的真实目录
            path = os.path.dirname(os.path.dirname(__file__))
            self.filenames = os.path.join(path, self.filenames)
            self._get_db_conf(self.filenames)
            self.conn_mysql(self.db_host, self.db_port, self.db_user, self.db_pass, self.db_database,
                            self.db_charset)

    # 使用conf配置文件连接msyql
    def _get_db_conf(self, filenames):
        self.conf.read(filenames)
        self.db_host = self.conf.get('db', 'db_host')
        self.db_port = self.conf.get('db', 'db_port')
        self.db_user = self.conf.get('db', 'db_user')
        self.db_pass = self.conf.get('db', 'db_pass')
        self.db_database = self.conf.get('db', 'db_database')
        self.db_charset = self.conf.get('db', 'db_charset')

    # pymysql连接msyql设置
    def conn_mysql(self, host, port, user, passwd, database, charset='utf8'):
        self.conn = pymysql.connect(host=host, port=int(port), user=user, passwd=passwd, database=database,
                                    charset=charset)
        self.cursor = self.conn.cursor()

        return self.cursor

    def insert_execute(self, insert_sql):
        self.cursor.execute(insert_sql)
        self.conn.commit()

    # @list_to_dict
    def get_data(self, tablename, *args):
        columns = ','.join(args)
        sql = 'select {} from {}'.format(columns, tablename)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def get_oneline(self, username):
        sql = 'select username,password from users where username="{}"'.format(username)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
