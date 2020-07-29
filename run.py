#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import argparse
import unittest
from common.variables import VariablePool
from utils.send_mail import send_report_mail
from utils.HTMLTestRunner import HTMLTestRunner


def running(path):
    """运行"""
    test_case = unittest.defaultTestLoader.discover('tests', 'test*.py')
    with open(path, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp,
                                title='Excel接口测试',
                                description="用例执行情况",
                                verbosity=2)
        result = runner.run(test_case)
    if result.failure_count:
        send_report_mail(path)


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="运行Excel接口测试")
    parser.add_argument('inputfile', type=str, help='原始文件')
    parser.add_argument('outputfile', type=str, help="输出文件")
    parser.add_argument('html', type=str, help="报告文件")
    args = parser.parse_args()

    def file_path(arg):
        if os.popen('pwd').read().strip() in arg:
            return arg
        else:
            return os.path.join(os.popen('pwd').read().strip(), arg)

    VariablePool.set('excel_input', file_path(args.inputfile))
    VariablePool.set('excel_output', file_path(args.outputfile))
    VariablePool.set('report_path', file_path(args.html))
    running(VariablePool.get('report_path'))


if __name__ == '__main__':
    main()
