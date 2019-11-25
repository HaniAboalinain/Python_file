# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 09:52:06 2019

@author: Hani
"""

class Person:
    # constructor or initializer
    def __init__(self, name):
        self.name = name
    
    # method which returns a string
    def whoami( self ):
        return "\n\nI am " + self.name
    
    # destructors
    def __del__( self ):
    print ( 'I have been deleted')


p1 = Person('Hani')
print(p1.whoami())
print(p1.name)
del p1
