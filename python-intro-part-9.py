#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 20:48:40 2019

@author: ccsheehan
Intro to Python course. Part 8
Lesson numbering began after the installation lesson.
Covers lists, tuples and dictionaries.
"""
#Lesson 22: Lists, Tuples and List Manipulation
    #tuples aren't mutable and can't be changed
    #tuples are used for variable assignments in sequence unpacking
def example():
    return 15,19
a,b = example()
#This is a tuple.
print(a)
print(b)
#Lists can be mutable. Lists are defined by square brackets. 
#There is no such thing as a python array unless you import it

x = [4,7,8,5,3,7,4,9,8]
print(x) #whole list
print(x[5]) #element of the list
x.append(12) #append adds to the end of the list
x.insert(5,7) #add something into a specific spot.
x.remove(7) #remove the 7. only removes the first seven in the list.
print(x.index(12)) #find index value 12
print(x.count(3)) #find the instances of 3 in the list
x.sort() #you can sort lists in order of numbers
#lists can also be strings

y = ['Spot', 'Cam', 'Jan', 'Dave', 'Zack']
print(y)
y.sort()
print(y) #orders alphabetically
y.reverse() #change the order of the list
'''
When you sort, it changes the value of the list. Keep that in mind.
If you don't want the order to be changed, then use a tuple
'''
#Lesson 23 Dictionaries
'''
Dictionaries are fairly similar to associated arrays in other languages.
They function more or less like data bases.
There are keys and values. Values can be repeated, but keys have to be one-of-a-kind
'''
#Teacher example

gradeDict = {'Student 1': 89, 'Student 2': 65, 'Student 3': 90, 'Student 4': 76} 
#curly brackets indicate dictionaries
#'Key': value

print(gradeDict) #whole dictionary
print(gradeDict['Student 2']) #print value of specific keys

gradeDict['Student 2'] = 56 #update values of keys

gradeDict['Student 5'] = 77 #add keys 

del gradeDict['Student 1'] #remove keys

print(gradeDict)

#update whole dictionary to have multiple values. You can indent dictionaries.

gradeDict = {'Student 1': [89, 88],
             'Student 2': [65, 70], 
             'Student 3': [90, 85], 
             'Student 4': [76, 89],
             'Student 5': [77, 80]
             }
#how to single out an individual value
print (gradeDict['Student 4'][0]) 
#the first value is in 0 place. Be careful with this!
