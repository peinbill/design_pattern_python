#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2025/3/9 16:02
# @Author      : Jim
# @File        : AbstractFacotry.py
# @Software    : PyCharm
# @Description :

from abc import ABC, abstractmethod


# 抽象控件和抽象工厂类
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class TextBox(ABC):
    @abstractmethod
    def paint(self):
        pass

class CheckBox(ABC):
    @abstractmethod
    def paint(self):
        pass

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_text_box(self) -> TextBox:
        pass

    @abstractmethod
    def create_check_box(self) -> CheckBox:
        pass

# 具体控件和具体工厂类
class WindowsButton(Button):
    def paint(self):
        print("Painting a Windows style button")

class WindowsTextBox(TextBox):
    def paint(self):
        print("Painting a Windows style text box")

class WindowsCheckBox(CheckBox):
    def paint(self):
        print("Painting a Windows style check box")

class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_text_box(self) -> TextBox:
        return WindowsTextBox()

    def create_check_box(self) -> CheckBox:
        return WindowsCheckBox()


class MacButton(Button):
    def paint(self):
        print("Painting a Mac style button")

class MacTextBox(TextBox):
    def paint(self):
        print("Painting a Mac style text box")

class MacCheckBox(CheckBox):
    def paint(self):
        print("Painting a Mac style check box")

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_text_box(self) -> TextBox:
        return MacTextBox()

    def create_check_box(self) -> CheckBox:
        return MacCheckBox()

def create_gui(factory: GUIFactory):
    button = factory.create_button()
    text_box = factory.create_text_box()
    check_box = factory.create_check_box()
    return button, text_box, check_box

windows_gui = create_gui(WindowsFactory())
mac_gui = create_gui(MacFactory())
