#!/usr/bin/env python3

# @FileName : conf_util.py
# @作者 : Liu
# @日期 : 2019年04月11日
# @时间 : 15时49分

from configparser import ConfigParser


class conf_util(object):

    def __init__(self, filenames=''):
        self.conf = ConfigParser()
        self.conf.read(filenames)
        self.value = None

    def get_conf_value(self, type_conf, conf_name):
        self.value = self.conf.get(type_conf, conf_name)
        return self.value


conf_util = conf_util


