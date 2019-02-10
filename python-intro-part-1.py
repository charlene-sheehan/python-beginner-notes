#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 17:39:14 2019

@author: ccsheehan

Intro to Python course. Part 1
Lesson 1 was the installation lesson.
Covers strings to if elif else statements
The triple quotes create a space for multi-line comments
"""
#lesson 2 strings (this is a single line comment initiated by the pound sign)

print('Hello World!')
print('Hello','World!')
print('I am', 24)
print("I'm 5")
print('I\'m 5')

#lesson 3 maths

print(1+3)
print(1-3)
print(1*3)
print(1/3)
print(4**2) #exponents
print(4**6) #exponents

#lesson 4 variables

exVar = 100 #integer variable
secondExVar = '100' #string variable
print(exVar)
print(secondExVar)

opVar = exVar / 5.3
print(opVar)

#lesson 5 while loops
condition = 1 #so easy to declare a variable!

while condition < 10: 
    print(condition)
    condition += 1 #plusequals adds one to the variable

'''
condition = 5
while condition < 15:
    print('True') 

This condition prints true infinitely because it will always be true.
Loop will never end
'''

condition = 5
while condition < 15:
    print('True')
    condition += 2

#lesson 6 for loops
exampleList = [1,6,74,3,2,0] #making a list
for x in exampleList:
    print('thing')
    
for x in range(1,11): #we have created a generator
    print(x)

#lesson 7 if statements

x = 2
y = 7
z = 10

if x> y:
    print(x,'is greater than',y) #this isn't going to run
if x < y:
    print(x,'is less than',y) #this does run
if x == y:
    print(x,'is the same as',y) #one equal sign is the assignment operator
    #two equal signs are the equal comparison operator

if x <= y:
    print('yes,',x,'is less than or equal to',y)
if z > y > x:
    print('yes,',z,'is the greatest number')
if z > y > x <= z > y:
    print('yes, this crazy statement works')    

#lesson 8 if else statements
    
if x == y:
    print('the same!')
else: #it will be a syntax error without the colon
    print('nope!') 

if x < y:
    print('finally, the truth')
else: 
    print('still wrong')

#lesson 9 if elif else statements a.k.a. how to stack if statements

if x > y:
    print('it is option one')
elif x < z:
    print('it is the second option')
else:
    print('neither option')

if x > y:
    print('it is option one')
elif x == z:
    print('it is the second option')
else:
    print('neither option')

if x > y:
    print('it is option one') 
elif x == z:
    print('it is the second option')
elif x < y < z:
    print('aha, it is the third option')
else:
    print('neither option')
'''
each condition will be checked one by one. 
once it finds a true statement, it will break
'''

if x > y or x < y: #hello or command! gives you options within the if statements
    print (x,'is smaller or larger than',y)

if x > y or x > z:
    print(x,'is the largest')
elif x > y: #you cannot use or with elif
    print(x,'is the middle number')
else:
    print(x,'is the little number')
    
