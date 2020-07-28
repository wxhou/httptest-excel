#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
from utils.logger import log
from common.variables import is_vars
from core.serialize import is_json_str


class Regular:
    """正则类"""

    def __init__(self):
        self.reg = re

    def finds(self, string):
        return self.reg.findall(r'\{{(.*?)}\}', string)

    def subs(self, keys, string):
        result = None
        log.info("提取变量：{}".format(keys))
        for i in keys:
            if is_vars.has(i):
                log.info("替换变量：{}".format(i))
                result = self.reg.sub(r"\{{%s}}" % i, is_vars.get(i), string)
        log.info("替换结果：{}".format(result))
        return result

    def find_res(self, exp, string):
        """在结果中查找"""
        if is_json_str(string):
            return self.reg.findall(r'\"%s":"(.*?)"' % exp, string)[0]
        else:
            return self.reg.findall(r'%s' % exp, string)[0]
