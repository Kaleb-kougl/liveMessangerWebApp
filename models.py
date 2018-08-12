import os

from flask import Flask


class Person:

    def __init__ (self, name):
        self.name = name

    def getName(self):
        if self.text is None:
            return "Empty"
        else:
            return self.name


class Message(Person):

    def __init__ (self, name, text):
        Person.__init__(self, name)
        self.text = text

    def getText(self):
        if self.text is None:
            return "Empty"
        else:
            return self.text
