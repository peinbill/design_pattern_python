#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2025/3/9 15:48
# @Author      : Jim
# @File        : Factory.py
# @Software    : PyCharm
# @Description :
from abc import ABC, abstractmethod

# 定义抽象产品类
class Product(ABC):
    @abstractmethod
    def use(self):
        pass

# 定义具体产品类 A
class ConcreteProductA(Product):
    def use(self):
        print("Using product A")

# 定义具体产品类 B
class ConcreteProductB(Product):
    def use(self):
        print("Using product B")

# 定义工厂类
class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        product.use()

# 定义具体工厂类 A
class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

# 定义具体工厂类 B
class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()

# 客户端代码
if __name__ == "__main__":
    creator_a = ConcreteCreatorA()
    creator_a.some_operation()

    creator_b = ConcreteCreatorB()
    creator_b.some_operation()
