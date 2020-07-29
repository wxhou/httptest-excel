#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from requests import Response
from utils.logger import log
from common.regular import Regular
from common.excelset import excel_set
from common.variables import VariablePool
from core.serialize import is_json_str, deserialization
from config import CF

reg = Regular()


def get_var_result(r: Response, number, case):
    """替换变量"""
    if case[CF.EXTRACT_VARIABLE]:
        for i in case[CF.EXTRACT_VARIABLE].split(','):
            result = reg.find_res(i, r.text)
            VariablePool.set(i, result)
            log.info(f"提取变量{i}={result}")
            if not VariablePool.get(i):
                excel_set.write_results(number, CF.EXTRACT_VARIABLE, f"提变量{i}失败")
    excel_set.write_results(number, CF.RESPONSE_TEXT,
                            f"ResponseCode：{r.status_code}\nResponseText：{r.text}")


def replace_param(case):
    """传入参数"""
    if case[CF.PARAMETER]:
        if is_json_str(case[CF.PARAMETER]):
            is_extract = reg.finds(case[CF.PARAMETER])
            if is_extract:
                return deserialization(reg.subs(is_extract, case[CF.PARAMETER]))
    return deserialization(case[CF.PARAMETER])
