#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class VariablePool:
    """全局变量池"""

    def get(self, name):
        """获取变量"""
        return getattr(self, name)

    def set(self, name, value):
        """设置变量"""
        setattr(self, name, value)

    def has(self, name):
        return hasattr(self, name)


is_vars = VariablePool()
