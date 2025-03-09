#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2025/3/9 15:03
# @Author      : Jim
# @File        : SimpleFactory.py
# @Software    : PyCharm
# @Description :
class Product:
    def operation(self):
        pass

class ConcreteProductA(Product):
    def operation(self):
        return "ConcreteProductA"

class ConcreteProductB(Product):
    def operation(self):
        return "ConcreteProductB"

class SimpleFactory:
    @staticmethod
    def create_product(product_type):
        if product_type == "A":
            return ConcreteProductA()
        elif product_type == "B":
            return ConcreteProductB()
        else:
            raise ValueError("Invalid product type")

if __name__ == "__main__":
    # 客户端代码
    product_a = SimpleFactory.create_product("A")
    product_b = SimpleFactory.create_product("B")

    print(product_a.operation())  # 输出：ConcreteProductA
    print(product_b.operation())  # 输出：ConcreteProductB
