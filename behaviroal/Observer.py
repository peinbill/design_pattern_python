#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2025/3/11 00:22
# @Author      : Jim
# @File        : Observer.py
# @Software    : PyCharm
# @Description :
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Observer:
    def update(self, subject):
        pass


class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state
        self.notify()


class ConcreteObserver(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, subject):
        print(f'{self._name} received an update: {subject.state}')


subject = ConcreteSubject()
observer1 = ConcreteObserver('Observer 1')
observer2 = ConcreteObserver('Observer 2')
subject.attach(observer1)
subject.attach(observer2)

subject.state = 123
subject.detach(observer1)

subject.state = 456
