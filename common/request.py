#!/usr/bin/env python
# coding=utf-8
import urllib3
import requests
from utils.logger import log
from requests.exceptions import RequestException

urllib3.disable_warnings()


class HttpRequest:
    """二次封装requests方法"""

    def __init__(self):
        self.r = requests.session()

    def send_request(self, method: str, url: str, **kwargs):
        """发送请求
        :param method: 发送方法
        :param url: 发送路径
        :param kwargs: 其他参数
        :return: request响应
        """
        pass
        method = method.upper()
        try:
            log.info("Request Url: {}".format(url))
            log.info("Request Method: {}".format(method))
            log.info("Request Data: {}".format(kwargs))
            if method == "GET":
                response = self.r.get(url, **kwargs)
            elif method == "POST":
                response = self.r.post(url, **kwargs)
            elif method == "PUT":
                response = self.r.put(url, **kwargs)
            elif method == "DELETE":
                response = self.r.delete(url, **kwargs)
            elif method in ("OPTIONS", "HEAD", "PATCH"):
                response = self.r.request(method, url, **kwargs)
            else:
                raise AttributeError("send request method is ERROR!")
            log.info(response)
            log.info("Response Data: {}".format(response.text))
            return response
        except RequestException as e:
            log.exception(format(e))
        except Exception as e:
            raise e

    def __call__(self, *args, **kwargs):
        return self.send_request(*args, **kwargs)


req = HttpRequest()
if __name__ == '__main__':
    log.info("你好")
