#!/usr/bin/env python3
# coding=utf-8
import os


class CF:
    """配置文件"""
    # 项目目录
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Excel首行配置
    NUMBER = 0
    NAME = 1
    METHOD = 2
    URL = 3
    ROUTE = 4
    HEADERS = 5
    PARAMETER = 6  # 参数
    EXPECTED_CODE = 7  # 预期响应码
    EXPECTED_REGULAR = 8  # 预期正则
    EXPECTED_VALUE = 9  # 预期结果值
    SPEND_TIME = 10  # 响应时间
    TEST_RESULTS = 11  # 测试结果
    EXTRACT_VARIABLE = 12  # 提取变量
    RESPONSE_TEXT = 13  # 响应文本
    # 字体大小
    FONT_SET = "微软雅黑"
    FONT_SIZE = 16
    # 颜色配置
    COLOR_PASSED = "90EE90"
    COLOR_FAILED = "FA8072"

    # 邮箱配置
    EMAIL_INFO = {
        'username': '1084502012@qq.com',
        'password': 2,
        'smtp_host': 'smtp.qq.com',
        'smtp_port': 465
    }
    # 收件人
    ADDRESSEE = ['1084502012@qq.com']


if __name__ == '__main__':
    print(CF.EXPECTED_CODE)
