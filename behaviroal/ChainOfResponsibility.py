#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2025/3/10 23:53
# @Author      : Jim
# @File        : ChainOfResponsibility.py
# @Software    : PyCharm
# @Description :

# 定义处理器接口
class Handler:
    def set_next(self, handler):
        pass

    def handle(self, request):
        pass

# 定义具体处理类
class AbstractHandler(Handler):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class ConcreteHandler1(AbstractHandler):
    def handle(self, request):
        if request == "request1":
            return "Handled by ConcreteHandler1"
        else:
            return super().handle(request)

class ConcreteHandler2(AbstractHandler):
    def handle(self, request):
        if request == "request2":
            return "Handled by ConcreteHandler2"
        else:
            return super().handle(request)

class ConcreteHandler3(AbstractHandler):
    def handle(self, request):
        if request == "request3":
            return "Handled by ConcreteHandler3"
        else:
            return super().handle(request)


# 处理类
handler1 = ConcreteHandler1()
handler2 = ConcreteHandler2()
handler3 = ConcreteHandler3()

handler1.set_next(handler2).set_next(handler3)

# 发送请求
requests = ["request1", "request2", "request3", "request4"]
for request in requests:
    response = handler1.handle(request)
    if response:
        print(response)
    else:
        print(f"{request} was not handled")

