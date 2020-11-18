#!/usr/bin/env python
# coding=utf-8
import urllib3
import requests
from config import CF
from utils.logger import log
from common.regular import Regular
from common.setResult import replace_param
from requests.exceptions import RequestException
from common.variables import VariablePool

urllib3.disable_warnings()


class HttpRequest:
    """二次封装requests方法"""

    http_method_names = 'get', 'post', 'put', 'delete', 'patch', 'head', 'options'

    def __init__(self):
        self.r = requests.session()
        self.reg = Regular()

    def deserialize(self, headers):
        """反序列化字典"""
        results = {}
        for i in headers.split('\n'):
            res = i.find(':')
            results[i[:res].strip()] = i[res + 1:].strip()
        return results

    def request(self, case, **kwargs):
        """发送请求
        :param case: 测试用例
        :param kwargs: 其他参数
        :return: request响应
        """
        if case[CF.URL]:
            VariablePool.set('url', case[CF.URL])
        if case[CF.HEADERS]:
            self.r.headers = self.deserialize(case[CF.HEADERS])
        method = case[CF.METHOD].upper()
        url = VariablePool.get('url') + case[CF.ROUTE]
        kwargs = replace_param(case[CF.PARAMETER])
        try:
            log.info("Request Url: {}".format(url))
            log.info("Request Method: {}".format(method))
            log.info("Request Data: {}".format(kwargs))

            def dispatch(method, *args, **kwargs):
                if method in self.http_method_names:
                    handler = getattr(self.r, method)
                    return handler(*args, **kwargs)
                else:
                    raise AttributeError('request method is ERROR!')
            response = dispatch(method.lower(), url, **kwargs)
            log.info(response)
            log.info("Response Data: {}".format(response.text))
            return response
        except RequestException as e:
            log.exception(format(e))
        except Exception as e:
            raise e
