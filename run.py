#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import unittest
from utils.HTMLTestRunner import HTMLTestRunner

test_case = unittest.defaultTestLoader.discover('tests', 'test*.py')

report_path = 'report/index.html'

if __name__ == '__main__':
    with open(report_path, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp,
                                title='Excel接口测试',
                                description="用例执行情况",
                                verbosity=2)
        runner.run(test_case)
