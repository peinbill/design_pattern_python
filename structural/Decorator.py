#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2025/3/9 23:36
# @Author      : Jim
# @File        : Decorator.py
# @Software    : PyCharm
# @Description :
from abc import ABC, abstractmethod

# 定义抽象组件
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

# 定义具体组件
class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"

# 定义抽象装饰器
class Decorator(Component):
    def __init__(self, component: Component):
        self._component = component

    @abstractmethod
    def operation(self):
        pass

# 定义具体装饰器 A
class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"ConcreteDecoratorA({self._component.operation()})"

# 定义具体装饰器 B
class ConcreteDecoratorB(Decorator):
    def operation(self):
        return f"ConcreteDecoratorB({self._component.operation()})"

if __name__ == "__main__":
    component = ConcreteComponent()
    decoratorA = ConcreteDecoratorA(component)
    decoratorB = ConcreteDecoratorB(decoratorA)
    print(decoratorB.operation())
