#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2025/3/11 00:14
# @Author      : Jim
# @File        : Mediator.py
# @Software    : PyCharm
# @Description :
from typing import List

class User:
    def __init__(self, name: str, mediator):
        self.name = name
        self.mediator = mediator

    def send_message(self, message: str):
        self.mediator.send_message(message, self)

    def receive_message(self, message: str):
        print(f"{self.name} received message: {message}")

class ChatRoom:
    def __init__(self):
        self.users: List[User] = []

    def add_user(self, user: User):
        self.users.append(user)

    def send_message(self, message: str, sender: User):
        for user in self.users:
            if user != sender:
                user.receive_message(f"{sender.name}: {message}")

if __name__ == '__main__':
    chat_room = ChatRoom()

    alice = User("Alice", chat_room)
    bob = User("Bob", chat_room)
    charlie = User("Charlie", chat_room)

    chat_room.add_user(alice)
    chat_room.add_user(bob)
    chat_room.add_user(charlie)

    alice.send_message("Hi everyone!")
    bob.send_message("Hello Alice!")
    charlie.send_message("Hey guys, what's up?")
