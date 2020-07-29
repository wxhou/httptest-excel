#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
from utils.logger import log
from common.variables import VariablePool
from core.serialize import is_json_str


class Regular:
    """正则类"""

    def __init__(self):
        self.reg = re.compile

    def finds(self, string):
        return self.reg(r'\{{(.*?)}\}').findall(string)

    def subs(self, keys, string):
        result = None
        log.info("提取变量：{}".format(keys))
        for i in keys:
            if VariablePool.has(i):
                log.info("替换变量：{}".format(i))
                comment = self.reg(r"\{{%s}}" % i)
                result = comment.sub(VariablePool.get(i), string)
        log.info("替换结果：{}".format(result))
        return result

    def find_res(self, exp, string):
        """在结果中查找"""
        if is_json_str(string):
            return self.reg(r'\"%s":"(.*?)"' % exp).findall(string)[0]
        else:
            return self.reg(r'%s' % exp).findall(string)[0]


if __name__ == '__main__':
    a = "{'data': {'loginName': 18291900215, 'password': '{{dd636482aca022}}', 'code': None, 'description': 'encrypt'}}"
    print(Regular().finds(a))
