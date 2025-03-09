#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2025/3/9 23:44
# @Author      : Jim
# @File        : Flyweight.py
# @Software    : PyCharm
# @Description :
class CharacterFactory:
    def __init__(self):
        self.characters = {}

    def get_character(self, character):
        if character in self.characters:
            return self.characters[character]
        else:
            new_character = Character(character)
            self.characters[character] = new_character
            return new_character

class Character:
    def __init__(self, character):
        self.character = character

    def render(self, font):
        print(f"Rendering character {self.character} in font {font}")

# 创建字符工厂
factory = CharacterFactory()

# 获取不同的字符
char1 = factory.get_character("A")
char2 = factory.get_character("B")
char3 = factory.get_character(" ")
char4 = factory.get_character(",")
char5 = factory.get_character(" ")
char6 = factory.get_character(".")

# 渲染不同的字符
char1.render("Arial")
char2.render("Times New Roman")
char3.render("Arial")
char4.render("Times New Roman")
char5.render("Arial")
char6.render("Times New Roman")
