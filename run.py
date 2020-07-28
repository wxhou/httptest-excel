#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import unittest
from config import CF
from utils.HTMLTestRunner import HTMLTestRunner

test_case = unittest.defaultTestLoader.discover('tests', 'test*.py')


def report_path():
    reports_path = os.path.join(CF.BASE_DIR, 'report')
    if not os.path.exists(reports_path):
        os.makedirs(reports_path)
    return os.path.join(reports_path, 'index.html')


if __name__ == '__main__':
    with open(report_path(), 'wb') as fp:
        runner = HTMLTestRunner(stream=fp,
                                title='Excel接口测试',
                                description="用例执行情况",
                                verbosity=2)
        runner.run(test_case)
