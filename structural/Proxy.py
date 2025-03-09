#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2025/3/9 23:47
# @Author      : Jim
# @File        : Proxy.py
# @Software    : PyCharm
# @Description :
# 抽象主题
class Email:
    def send(self, message):
        pass


# 真实主题
class EmailServer(Email):
    def send(self, message):
        print(f'Sending email: {message}')


# 代理主题
class EmailProxy(Email):
    def __init__(self, email_server):
        self.email_server = email_server

    def send(self, message):
        if self.is_allowed_to_send(message):
            self.email_server.send(message)
            self.log(message)
        else:
            print('Not allowed to send email')

    def is_allowed_to_send(self, message):
        # Check if user is allowed to send the email
        return True

    def log(self, message):
        # Log the email to a file
        print(f'Logging email: {message}')


# 客户端
if __name__ == '__main__':
    email_server = EmailServer()
    email_proxy = EmailProxy(email_server)
    email_proxy.send('Hello, world!')
