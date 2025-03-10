#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2025/3/11 00:04
# @Author      : Jim
# @File        : Interpreter.py
# @Software    : PyCharm
# @Description :
class Context:
    def __init__(self):
        self._variables = {}

    def set_variable(self, name, value):
        self._variables[name] = value

    def get_variable(self, name):
        return self._variables.get(name)


class Expression:
    def interpret(self, context):
        pass


class VariableExpression(Expression):
    def __init__(self, name):
        self._name = name

    def interpret(self, context):
        return context.get_variable(self._name)


class ConstantExpression(Expression):
    def __init__(self, value):
        self._value = value

    def interpret(self, context):
        return self._value


class AddExpression(Expression):
    def __init__(self, left, right):
        self._left = left
        self._right = right

    def interpret(self, context):
        return self._left.interpret(context) + self._right.interpret(context)


class SubtractExpression(Expression):
    def __init__(self, left, right):
        self._left = left
        self._right = right

    def interpret(self, context):
        return self._left.interpret(context) - self._right.interpret(context)

if __name__ =="__main__":
    # 测试代码
    context = Context()
    a = ConstantExpression(1)
    b = ConstantExpression(2)
    c = ConstantExpression(3)
    x = VariableExpression('x')
    y = VariableExpression('y')

    context.set_variable('x', 10)
    context.set_variable('y', 5)

    # 1 + 2 + 3 = 6
    expression = AddExpression(AddExpression(a, b), c)
    result = expression.interpret(context)
    print(result)

    # 10 - 2 + 5 = 13
    expression = AddExpression(SubtractExpression(x, b), y)
    result = expression.interpret(context)
    print(result)
