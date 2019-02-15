#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 18:48:49 2019

@author: ccsheehan

Intro to Python course. Part 2
Lesson numbering began after the installation lesson.
Covers functions to ?
"""
#lesson 10 functions

x = 1
y = 3

print(x+y)

def myFirstFunction():
    x = 1
    y = 3
    print(x+y)
    if x < y:
        print(x,'is the little one')
    
myFirstFunction()

#example teacher uses is a spell checker

#lesson 11 function parameters
#example is making a calculator
def addition(num1,num2,num3,num4):
    answer = num1+num2+num3+num4
    return answer
 
x = addition(5,6,6,5)
print(x)

#wordpress, website example
def website(font,background_colour,fontsize,fontcolour):
    print('font:',font)
    print('bg:',background_colour)
    print('Font size:',fontsize)
    print('Font colour:',fontcolour)

website('TNR','white','11','black')
#how to make it order independent
website(font='TNR',
        fontsize='11',
        fontcolour='white',
        background_colour='white')
#but what if you have over 100 variables?! you make defaults
'''
new code would look like this:
def website(font='TNR',background_colour='white',fontsize,fontcolour):
    print('font:',font)
    print('bg:',background_colour)
    print('Font size:',fontsize)
    print('Font colour:',fontcolour)
'''
#lesson 12 global and local variables
'''
global variable: accessed anywhere, but cannot be modified locally
local variable: accessed and modified in its local environment, can't be
                applied outside of that environment
'''
x = 6 #this is the global variable
def example():
    z = 5 #this is the local variable
    print (z)
'''    
print(z) 
can't do this because z is limited to within its environment
'''
def example2():
    z = 7
    print(z)
    y = x + 1 #you can ACCESS the global variable, but cannot export it
    print (y) #creating y gets rid of the problem of the function modifying x
    return y 
x = example2()
print(x)
#BEST PRACTICE right here 
#this redefines x properly
'''
global variables in functions are possible, 
but not best practice because globals can get messy in complex scripts
many employers want the cleanest code
'''
def example3():
  global x #just because you can do it doesn't mean you should
  x+=1
  print(x)  
 
'''
example2 is the preferred method
'''

    


