#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2025/3/11 00:35
# @Author      : Jim
# @File        : TemplateMethod.py
# @Software    : PyCharm
# @Description :
# 抽象类，定义算法的骨架
class CoffeeMaker:
    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()

    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring into cup")

    # 抽象方法，需要子类实现
    def brew(self):
        pass

    # 钩子方法，影响算法的执行
    def customer_wants_condiments(self):
        return True

    # 具体方法，提供默认实现
    def add_condiments(self):
        print("Adding sugar and milk")


# 具体子类，实现抽象方法和钩子方法
class Coffee(CoffeeMaker):
    def brew(self):
        print("Brewing coffee")

    def customer_wants_condiments(self):
        answer = input("Would you like sugar and milk with your coffee? (y/n)")
        return answer.lower().startswith('y')


# 使用具体子类冲泡咖啡
if __name__ == '__main__':
    coffee = Coffee()
    coffee.prepare()
