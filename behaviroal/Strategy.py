#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2025/3/11 00:32
# @Author      : Jim
# @File        : Strategy.py
# @Software    : PyCharm
# @Description :

# 策略接口
class SortStrategy:
    def sort(self, data):
        pass

# 具体策略类
class QuickSort(SortStrategy):
    def sort(self, data):
        # 使用快速排序算法实现排序
        pass

class BubbleSort(SortStrategy):
    def sort(self, data):
        # 使用冒泡排序算法实现排序
        pass


# 定义上下文类
class SortContext:
    def __init__(self):
        self.strategy = None

    def set_sort_strategy(self, strategy):
        self.strategy = strategy

    def sort_data(self, data):
        self.strategy.sort(data)

# 客户端
context = SortContext()
data = [5, 1, 4, 2, 8]

context.set_sort_strategy(QuickSort())
context.sort_data(data)  # 使用快速排序算法实现排序

context.set_sort_strategy(BubbleSort())
context.sort_data(data)  # 使用冒泡排序算法实现排序












