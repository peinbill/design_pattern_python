#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2025/3/10 23:58
# @Author      : Jim
# @File        : Command.py
# @Software    : PyCharm
# @Description :

# 定义Command接口
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# 实现具体命令类
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


# Invoker
class RemoteControl:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def execute_commands(self):
        for command in self.commands:
            command.execute()

# Receiver
class Light:
    def turn_on(self):
        print("The light is on")

    def turn_off(self):
        print("The light is off")


# 创建并使用命令
light = Light()

remote_control = RemoteControl()
remote_control.add_command(LightOnCommand(light))
remote_control.add_command(LightOffCommand(light))

remote_control.execute_commands()
