#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 14:48:38 2017

@author: wbreen
"""

def main():
    file = findFileName()
    #read in the file
    #Create a dictionary based on the file (two words are the key, and the next word is the value)
    #The dictionary values should be a list
    dictionary = createDic(file)
    
    #take the first two words from the file and print them
    #use the preceding two words to be the lookup values for the next word to use
    #do this up until it has printed 500 words
    #printNewText()
    
#This method gets the file that the Dictionary will be based off of
def findFileName():
    fileName = input("Give me the name of the file you want to confound: ")
    correctEnd = ".txt"
    
    if fileName[-4:] != correctEnd :
        fileName += ".txt"
    
    #print(fileName)
    return fileName
        
#findFileName()

#Given the filename, use that to create a dictionary of 2 words, 1 word
def createDic(fileName):
    twoWordDic = {}
    myFile = open(fileName,'r')
    wordList = []
    
    for line in myFile:
        splitLine = line.split()
        for word in splitLine:
            wordList.append(word)
            #made the list of words
            
    #now take the list of words, loop through them,
    
    for i in wordList:
        print(i)
        #Need to get the word at the index i, and then you can do this more easily
        key, value = wordList[i:i+1], wordList[i+2]
        print(key)
        print(value)
        #twoWordDic[key]=value
        
    #print(wordList)
            
    #Maybe go through the words 3 at a time, then create a new key in the dictionary each time  
def addToDic(dictionary, word1, word2, word3):
    dictionary[word1+" "+word2]=word3

       
main()