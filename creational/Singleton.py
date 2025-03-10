#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2025/3/9 16:17
# @Author      : Jim
# @File        : Singleton.py
# @Software    : PyCharm
# @Description :

class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

if __name__ == "__main__":
    s1 = Singleton.get_instance()
    s2 = Singleton.get_instance()

    print(s1 is s2)  # True
