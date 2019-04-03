#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 20:27:45 2019

@author: ccsheehan
Intro to Python course. Part 6
Lesson numbering began after the installation lesson.
Covers inputs and a little statistics, importing modules
"""
#Lesson 19 Inputs and Import Syntax

#raw input is just input in python3
#how to get information from users!
name = input('What is your name?: ')
print('Hello', name)
#add a space because the user will enter next to it.

#import as!! So clutch to make code less redundant

import statistics as s

exList = [5,6,4,5,6,7,45,68,33,55]

print(s.mean(exList))

#but what if we only want the mean from the stats?

from statistics import mean

print(mean(exList))

#same result!
from statistics import mean, stdev
print(stdev(exList))
#can make even shorter as well
from statistics import mean as m, stdev as s
print(s(exList))
print(m(exList))
#if you want everything from statistics module
from statistics import *
print(stdev(exList))

