#!/usr/bin/env python
# coding=utf-8
import re
import unittest
from config import CF
from utils.logger import log
from common.request import req
from common.excelset import ExcelSet


class TestApi(unittest.TestCase):
    """测试接口"""

    def test_api(self):
        """
        测试excel接口用例
        """
        exs = ExcelSet()
        cases = exs.get_cases()
        for number, case in cases:
            log.info("开始执行用例：{}".format(case))
            method = case[CF.METHOD]
            url = case[CF.URL]
            headers = case[CF.HEADERS]
            parameter = case[CF.PARAMETER]
            r = req(method, url, case[CF.ROUTE], headers=headers, **parameter if parameter else None)
            test_result = r.status_code == case[CF.EXPECTED_CODE]
            if test_result and case[CF.EXPECTED_VALUE]:
                test_result = case[CF.EXPECTED_VALUE] in r.text
                log.info("预期值结果：{}".format(test_result))
            if test_result and case[CF.EXPECTED_REGULAR]:
                test_result = re.findall(r'%s' % case[CF.EXPECTED_VALUE], r.text)
                log.info("正则结果：{}".format(test_result))
            exs.write_results(number, CF.TEST_RESULTS, 'PASS' if test_result else 'FAILED')
            exs.write_results(number, CF.SPEND_TIME, r.elapsed.total_seconds())


if __name__ == '__main__':
    unittest.main(verbosity=2)
