#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json


def deserialization(content: json):
    """
    反序列化
        json对象 -> python数据类型
    """
    return json.loads(content)


def serialization(content, ensure_ascii=True):
    """
    序列化
        python数据类型 -> json对象
    """
    return json.dumps(content, ensure_ascii=ensure_ascii)


def is_json_str(string):
    """判断是否是json格式字符串"""
    if isinstance(string, str):
        try:
            json.loads(string)
            return True
        except ValueError:
            return False
    return False


if __name__ == '__main__':
    a = "{'data': {'loginName': 18291900215, 'password': 'dd636482aca022', 'code': None, 'description': 'encrypt'}}"
    print(is_json_str(a))
