#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 14:48:38 2017

@author: William Breen
"""

def main():
    file = findFileName()
    #read in the file
    #Create a dictionary based on the file (two words are the key, and the next word is the value)
    #The dictionary values should be a list
    wordList = createList(file)
    dictionary = createDic(wordList)
    #createNewText(wordList, dictionary)
    
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
   
#given the list of words from the file, create a dictionary from them in the form of [(word, Times it appears)]
def createDic(wordList):
    twoWordDic = {}
    for i in range(len(wordList)-2):
        
        key = wordList[i]+" "+wordList[i+1]
        value = wordList[i+2]
        #if the key already exists in the dictionary, compare the new value to the old values, if they match, then add 1 to the second part of the tuple
        
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
    
    print(twoWordDic)
    return twoWordDic






#Method creates the new 500 words that sound like the old text
def createNewText(words, dictionary):
    #start with the first two words of the old text
    finalText = ""
    finalTextList = []
    finalTextList.append(words[0])
    finalTextList.append(words[1])
    
    for i in range(150):
        key = finalTextList[-2]+" " +finalTextList[-1]
        #print (key,"this is the key")
        nextWord = dictionary.get(key)
        #print(nextWord)
        finalTextList.append(nextWord)
    finalText = ' '.join(finalTextList)
    print(finalText)

    

main()



































