#!/usr/bin/env python
# coding=utf-8
import os
import openpyxl
from config import CF
from utils.logger import log
from openpyxl.styles import PatternFill


class ExcelSet:
    """配置"""

    def __init__(self):
        self.path = os.path.join(CF.BASE_DIR, 'data', 'usercase.xlsx')
        self.wb = openpyxl.load_workbook(self.path)
        self.table = self.wb.active

    def get_cases(self, min_row=2):
        """获取用例"""
        all_cases = []
        for row in self.table.iter_rows(min_row=min_row):
            all_cases.append((min_row, [cell.value for cell in row]))
            min_row += 1
        return all_cases

    def write_results(self, row_n, col_n, value):
        """写入结果"""
        cell = self.table.cell(row_n, col_n + 1)
        cell.value = value
        if value.lower() == "fail":
            fill = PatternFill("solid", fgColor="FF0000")
            cell.fill = fill
        elif value.lower() == "pass":
            fill = PatternFill("solid", fgColor="00CD00")
            cell.fill = fill
        self.wb.save(self.path)


if __name__ == '__main__':
    read = ExcelSet()
    print(read.get_cases())
