#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2025/3/11 00:29
# @Author      : Jim
# @File        : State.py
# @Software    : PyCharm
# @Description :



# 抽象状态类
class State:
    def handle(self):
        pass

# 具体状态类
class OpenState(State):
    def handle(self):
        print("Opening the door")

class CloseState(State):
    def handle(self):
        print("Closing the door")

class RunState(State):
    def handle(self):
        print("Running")


# 环境类
class Lift:
    def __init__(self):
        self.state = None

    def setState(self, state):
        self.state = state

    def open(self):
        self.state.handle()

    def close(self):
        self.state.handle()

    def run(self):
        self.state.handle()

# 应用
lift = Lift()
lift.setState(OpenState())
lift.open() # Opening the door

lift.setState(CloseState())
lift.close() # Closing the door

lift.setState(RunState())
lift.run() # Running















