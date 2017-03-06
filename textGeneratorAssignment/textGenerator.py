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
    wordList = createList(file)
    dictionary = createDic(wordList)
    createNewText(wordList, dictionary)
    
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
            
    #print(wordList)
    return wordList
   
#given the list of words from the file, create a dictionary from them
def createDic(wordList):
    twoWordDic = {}
    for i in range(len(wordList)-2):
        #Need to get the word at the index i, and then you can do this more easily
        key, value = wordList[i]+" "+wordList[i+1], wordList[i+2]
        #print("Key = "+key, "Value = "+ value)
        
        twoWordDic[key]=value
    
    #print(twoWordDic)
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



































