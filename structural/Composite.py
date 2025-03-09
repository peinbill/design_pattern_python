#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2025/3/9 23:29
# @Author      : Jim
# @File        : Composite.py
# @Software    : PyCharm
# @Description :
from abc import ABC, abstractmethod

# 抽象组件
class FileComponent(ABC):
    @abstractmethod
    def list(self):
        pass

# 叶子组件
class File(FileComponent):
    def __init__(self, name):
        self.name = name

    def list(self):
        print(self.name)

# 容器组件
class Folder(FileComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def list(self):
        print(self.name)
        for child in self.children:
            child.list()

# 客户端
root = Folder("root")
folder1 = Folder("folder1")
folder2 = Folder("folder2")
file1 = File("file1")
file2 = File("file2")

root.add(folder1)
root.add(folder2)
root.add(file1)
folder1.add(file2)

root.list()
