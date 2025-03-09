#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2025/3/9 22:53
# @Author      : Jim
# @File        : Prototype.py
# @Software    : PyCharm
# @Description :
import copy

class Prototype:
    def __init__(self, x, y, items):
        self.x = x
        self.y = y
        self.items = items

    def clone(self):
        return copy.deepcopy(self)

if __name__ == '__main__':
    items = ['item1', 'item2', 'item3']
    original = Prototype(1, 2, items)
    # 接下来，客户端代码更新原型对象的成员，但是新对象不会受到影响，因为它们共享的是不同的内存空间。
    clone = original.clone()

    print(f'Original: x={original.x}, y={original.y}, items={original.items}')
    print(f'Clone: x={clone.x}, y={clone.y}, items={clone.items}')

    items.append('item4')
    original.x = 5
    original.y = 10

    print(f'Original (updated): x={original.x}, y={original.y}, items={original.items}')
    print(f'Clone (not updated): x={clone.x}, y={clone.y}, items={clone.items}')
