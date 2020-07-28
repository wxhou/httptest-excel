#!/usr/bin/env python3
# coding=utf-8
import logging
import os
from datetime import datetime

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Logger:
    def __init__(self):
        log_path = self.log_path[:self.log_path.rfind('/')]
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        self.logger = logging.getLogger()
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)

            # 创建一个handler，用于写入日志文件
            fh = logging.FileHandler(self.log_path, encoding='utf-8')
            fh.setLevel(logging.DEBUG)

            # 再创建一个handler，用于输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            # 定义handler的输出格式
            formatter = logging.Formatter(self.fmt)
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # 给logger添加handler
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    @property
    def log_path(self):
        now_month = datetime.now().strftime("%Y%m")
        return os.path.join(root_dir, 'logs', '{}.log'.format(now_month))

    @property
    def fmt(self):
        return '%(levelname)s %(asctime)s %(filename)s:%(lineno)d %(message)s'


log = Logger().logger
if __name__ == '__main__':
    log.info("你好")
