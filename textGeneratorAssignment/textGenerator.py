#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 14:48:38 2017

@author: William Breen
@copyright: William Breen 2017
"""

def main():
    #read in file
    file = findFileName()
    #Create list of words in the file
    wordList = createList(file)
    #Create a dictonary from that list
    dictionary = createDic(wordList)
    #Use the dictionary to create a new sounds-like text, and print it
    createNewText(wordList, dictionary)
    
    
#This method gets the file that the Dictionary will be based off of
def findFileName():
    fileName = input("Give me the name of the file you want to imitate: ")
    correctEnd = ".txt"
    
    if fileName[-4:] != correctEnd :
        fileName += ".txt"
    return fileName


#Given the filename, use that to create a list of the words in the file of 2 words, 1 word
def createList(fileName):
    myFile = open(fileName,'r')
    wordList = []
    
    for line in myFile:
        splitLine = line.split()
        for word in splitLine:
            wordList.append(word)
            #made the list of words
            
    return wordList
   
#given the list of words from the file, create a dictionary from them in the form of [(word, # times it appears)]
def createDic(wordList):
    twoWordDic = {}
    for i in range(len(wordList)-2):
        key = wordList[i]+" "+wordList[i+1]
        value = wordList[i+2]
        #Creates a dictionary with just the key and the value of the word repeated over and over, will compress this in the second part of the method
        if key in twoWordDic:
            currentVals = twoWordDic.get(key)
            keyWordValues = []
            for oldValue in currentVals:
                keyWordValues.append(oldValue)
                    
            newValue = (value)
            keyWordValues.append(newValue)
            twoWordDic[key] = keyWordValues
            
        else: 
            twoWordDic[key]=[value]
    
    #take the dictionary that has been created, and now compresses them into just one dictionary in the correct form
    for key in twoWordDic:
        #for each key, get the value of the key
        #Read each value into its own list
        #go through the list, count the number of times the first element occurs, and append it into a new list
        #before adding to the new list, see if the new list contains the element you are trying to append
            #if it doesn't contain the element, append it, if it does contain the element, don't do anything
        myValues = twoWordDic[key]
        newList = []
        for value in myValues:
            numOfValues = myValues.count(value)
            newValue = value, numOfValues
            if newList.count(newValue) is 0:
                newList.append(newValue)
            else:
                newList = newList
                
        twoWordDic[key] = newList
    #sort the dictionary so the most frequently used words are first
    sortDictionary(twoWordDic)
    
    return twoWordDic

    
#Sorts the dictionary based on the number of times a number has been used
def sortDictionary(dictionary):
    for key in dictionary:
        valuesList = dictionary.get(key)
        valuesList = sorted(valuesList, key=lambda v: (-1*v[1], v[0].lower()))
        dictionary[key]=valuesList
        
    return dictionary


#Method creates the new 500 words that sound like the old text
def createNewText(words, dictionary):
    #start with the first two words of the old text
    finalText = ""
    finalTextList = []
    
    finalTextList.append(words[0])
    finalTextList.append(words[1])
    space = " "
    
    for i in range(500):
        key = space.join(finalTextList[-2:])
        wordToAdd = retrieveFrequentUse(dictionary, key)
        finalTextList.append(wordToAdd)
        
        valToRemove = dictionary.get(key)
        removeIfMoreValues(dictionary, key, valToRemove[0])
        
    finalText = ' '.join(finalTextList)
    print(finalText)

        
#This method will return the most frequently used word from the list in the dictionary
def retrieveFrequentUse(dictionary, key):
    myList = dictionary.get(key)
    myList = sorted(myList, key=lambda m: (-1*m[1],m[0].lower()))
    return myList[0][0]

#Removes the value given from the dictionary at the key value if there are other possibilities for the key
def removeIfMoreValues(dictionary, key, value):
    listOfValues = dictionary.get(key)
    #if there are more values in the list than just 1, then remove the first one (the value)
    if len(listOfValues)>1:
        listOfValues.remove(value)
        
    dictionary[key]=listOfValues

    
    

main()



































