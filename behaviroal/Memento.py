#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2025/3/11 00:19
# @Author      : Jim
# @File        : Memento.py
# @Software    : PyCharm
# @Description :
import copy

# 发起人类
class Originator:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        print("设置状态为：", state)
        self._state = state

    def create_memento(self):
        print("创建备忘录")
        return Memento(copy.deepcopy(self._state))

    def restore_memento(self, memento):
        print("恢复备忘录")
        self._state = memento.get_state()

    def show_state(self):
        print("当前状态为：", self._state)

# 备忘录类
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

# 管理者类
class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]

# 测试
if __name__ == "__main__":
    originator = Originator()
    caretaker = Caretaker()

    originator.set_state("状态1")
    caretaker.add_memento(originator.create_memento())

    originator.set_state("状态2")
    caretaker.add_memento(originator.create_memento())

    originator.set_state("状态3")
    originator.show_state()

    originator.restore_memento(caretaker.get_memento(1))
    originator.show_state()

    originator.restore_memento(caretaker.get_memento(0))
    originator.show_state()
