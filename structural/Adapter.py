#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2025/3/9 23:07
# @Author      : Jim
# @File        : Adapter.py
# @Software    : PyCharm
# @Description :
# 目标接口
class Target:
    def request(self):
        pass

# 源接口
class Adaptee:
    def specific_request(self):
        pass

# 类适配器
class Adapter(Target, Adaptee):
    def request(self):
        self.specific_request()
        # 其他逻辑

# 对象适配器
class Adapter2(Target):
    def __init__(self, adaptee):
        self._adaptee = adaptee

    def request(self):
        self._adaptee.specific_request()
        # 其他逻辑

# 客户端代码
def client_code(target):
    target.request()

adaptee = Adaptee()
adapter = Adapter()
adapter2 = Adapter2(adaptee)

client_code(adapter)
client_code(adapter2)
