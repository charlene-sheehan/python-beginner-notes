#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 19:30:44 2019

@author: ccsheehan
Intro to Python course. Part 5
Lesson numbering began after the installation lesson.
Covers classes
Very basic introduction to classes for the purposes of:
    how to create one; how to read one to see the intent of the author
Calculator example is used
"""
#Lesson 17 Classes
#the word class can be used to define a class
class calc: 
#classes embed functions
    def add(x,y):
        answer = x + y
        print(answer)
        
    def sub(x,y):
        answer = x - y
        print(answer)
    
    def mult(x,y):
        answer = x * y
        print(answer)
    
    def div(x,y):
        answer = x / y
        print(answer)
#I have added an exponent function as well to reinforce previous knowledge
    # the exponent function is not included in the original lesson
    def expo(x,y):
        answer = x ** y
        print(answer)

#Tada, we have put together a class. Decrease the indent to end (or close?) the class

calc.add(5,3) #this returns 8. success!
calc.sub(5,3) 
calc.mult(5,3)
calc.div(5,3)
calc.expo(5,3) #double success - my function worked!
