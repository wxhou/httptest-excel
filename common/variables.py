#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class VariablePool:
    """全局变量池"""

    @staticmethod
    def get(name):
        """获取变量"""
        return getattr(VariablePool, name)

    @staticmethod
    def set(name, value):
        """设置变量"""
        setattr(VariablePool, name, value)

    @staticmethod
    def has(name):
        return hasattr(VariablePool, name)


if __name__ == '__main__':
    VariablePool.set('name', 'wxhou')
    print(VariablePool.get('name'))
