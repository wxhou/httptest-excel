#!/usr/bin/env python
# coding=utf-8
import unittest
from parameterized import parameterized
from common.excelset import ExcelSet
from core.request import HttpRequest
from common.checkResult import check_result
from common.setResult import get_var_result

excel_set = ExcelSet()


class TestApi(unittest.TestCase):
    """测试接口"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.req = HttpRequest()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.req.r.close()

    @parameterized.expand(excel_set.get_cases())
    def test_api(self, name, number, case):
        """
        测试excel接口用例
        """
        r = self.req.send_request(case)
        get_var_result(r, number, case)
        check_result(r, number, case)


if __name__ == '__main__':
    unittest.main(verbosity=2)
