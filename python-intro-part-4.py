#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 21:21:16 2019

@author: ccsheehan
Intro to Python course. Part 4
Lesson numbering began after the installation lesson.
Covers writing, appending and reading files
Note: You should manipulate the multi-line comments to try out the different functions
Besides the lesson titles, inline comments (the pound key/hashtag) are notes on the nearest line of code.
"""
#Lesson 14 Writing to a file. Only writes this data; wipes out anything already there
'''
writeMe = 'Example text'
saveFile = open('exampleWrite.txt','w') #the w is key
#when you write a file, you create or rewrite one.
saveFile.write(writeMe) #written but not saved!
saveFile.close() #this will close the file and save the contents. if the file exists, it will overwrite.
'''
#Lesson 15 Appending to a file. This adds to the end of a file
'''
appendMe = 'And even more text'
saveFile = open('exampleWrite.txt', 'a') #like above, the a is key
saveFile.write('\n') #add more specifics to appending the document. moves text to a new line and then adds it
saveFile.write(appendMe)
saveFile.close()

how to make a new line  saveFile.write('\n')
how to tab saveFile.write('\t')
how to add a space saveFile.write('\s')
'''

#Lesson 16 Reading from a file and printing contents to the console
'''
readMe = open('exampleWrite.txt','r').read()
print(readMe) #prints the contents of the text file to the console

splitMe = readMe.split('\n') #this creates a python list!

print(splitMe[3])

#another, easier way to do this
readMe2 = open('exampleWrite.txt','r').readlines()
print(readMe2)
#read lines puts the lines into a list for you, but it includes the \n in the printed contents
'''