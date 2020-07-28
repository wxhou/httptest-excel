#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
from config import CF
from utils.logger import log
from requests import Response
from common.excelset import ExcelSet

excel_set = ExcelSet()


def check_result(r: Response, number, case):
    """获取结果"""
    results = []
    excel_set.write_results(number, CF.SPEND_TIME, r.elapsed.total_seconds(), color=False)
    if case[CF.EXPECTED_CODE]:
        results.append(int(case[CF.EXPECTED_CODE]) == r.status_code)
        log.info(f"预期响应码：{case[CF.EXPECTED_CODE]},实际响应码：{r.status_code}")
    if case[CF.EXPECTED_VALUE]:
        results.append(case[CF.EXPECTED_VALUE] in r.text)
        log.info(f"预期响应值：{case[CF.EXPECTED_VALUE]},实际响应值：{r.text}")
    if case[CF.EXPECTED_REGULAR]:
        res = r'%s' % case[CF.EXPECTED_REGULAR]
        ref = re.findall(res, r.text)
        results.append(ref)
        log.info(f"预期正则：{res},响应{ref}")
    if all(results):
        excel_set.write_results(number, CF.TEST_RESULTS, 'Pass')
        log.info(f"用例【{case[CF.NAME]}】测试成功！")
    else:
        excel_set.write_results(number, CF.TEST_RESULTS, 'Failed')
        assert all(results), f"用例【{case[CF.NUMBER]}{case[CF.NAME]}】测试失败：{results}"
