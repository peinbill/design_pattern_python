#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2025/3/11 00:09
# @Author      : Jim
# @File        : Iterator.py
# @Software    : PyCharm
# @Description :
from abc import ABC, abstractmethod

# 抽象迭代器类
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

# 具体迭代器类
class ConcreteIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.index = 0

    def has_next(self):
        return self.index < len(self.data)

    def next(self):
        if self.has_next():
            value = self.data[self.index]
            self.index += 1
            return value

# 抽象聚合类
class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

# 具体聚合类
class ConcreteAggregate(Aggregate):
    def __init__(self, data):
        self.data = data

    def create_iterator(self):
        return ConcreteIterator(self.data)

# 测试
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    aggregate = ConcreteAggregate(data)
    iterator = aggregate.create_iterator()

    while iterator.has_next():
        print(iterator.next())
