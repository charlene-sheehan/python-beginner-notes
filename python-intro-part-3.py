#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 18:55:35 2019

@author: ccsheehan
Intro to Python course. Part 3
Lesson numbering began after the installation lesson.
Covers common python errors
"""
#Lesson 13 Common Python Errors
'''
Be weary of typos and random indents. 
'''

variable = 55
'''
name error
print(varaible) so easy to overlook - causes name error
NameError: name 'varaible' is not defined
'''

'''
indentation error

def func1():
    
def func2():
    print(2)
    
IndentationError: expected an indented block
'''

def task():
    print('1')
print('2') #when you change the indent, Python is signaled that you're done
''' 
  print('3') what is this?!
 IndentationError: unexpected indent
''' 
 
'''
print('Hey there how are you today?'

      automatic indent? what happened> oh, I forgot the bracket
'''
# x = [1,2,3,4 ---> neverending list!! forgotten bracket

'''
Different type of issue:
    running incompatible python modules.
    64 bit module needs a machine that can run it.
    Always check the bit for compatibility.
    A 64 bit capable machine can run 32 bit, but not vice versa
'''

