#!/usr/bin/env python
# coding=utf-8
import os
import openpyxl
from config import CF
from openpyxl.styles import Font
from openpyxl.styles import PatternFill


class ExcelSet:
    """Excel配置"""

    def __init__(self):
        self.path = os.path.join(CF.BASE_DIR, 'data', 'usercase.xlsx')
        self.wb = openpyxl.load_workbook(self.path)
        self.table = self.wb.active

    def get_cases(self, min_row=2):
        """获取用例"""
        all_cases = []
        for row in self.table.iter_rows(min_row=min_row):
            all_cases.append((self.table.cell(min_row, CF.NAME + 1).value,
                              min_row, [cell.value for cell in row]))
            min_row += 1
        return all_cases

    def write_results(self, row_n, col_n, value, color=True):
        """写入结果"""
        cell = self.table.cell(row_n, col_n + 1)
        cell.value = value
        font = Font(name='微软雅黑', size=16)
        cell.font = font
        if color:
            if value.lower() in ("fail", 'failed'):
                fill = PatternFill("solid", fgColor="FF0000")
                cell.fill = fill
            elif value.lower() in ("pass", "ok"):
                fill = PatternFill("solid", fgColor="00CD00")
                cell.fill = fill
        self.wb.save(self.path)


if __name__ == '__main__':
    read = ExcelSet()
    print(read.get_cases())
