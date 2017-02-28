# -*- coding: utf-8 -*-
#William Breen, (The pound key is how you do comments)
#Talk like a Pirate

#import sys
import random

def createDictionary():
    pirateDic = {}
    infile = open("Translation.txt", 'r')
    for line in infile.readlines():
        english, pirate = line.strip().split(":")
        pirateDic[english]=pirate
    return pirateDic
        
#print(createDictionary())

def readInput():
    #reads the input and changes it to the pirate version
    pirateDic = createDictionary()
    line = input("Enter a phrase:")
    
    while (line != "quit"):
        keys = pirateDic.keys()
        for key in keys:
            #Still need to fix bug about not finding the key in the middle of words
            keyLoc = line.find(key)
            space, notFound = " ", -1
            if line.find(space,keyLoc-1,keyLoc+1) is notFound:
                line=line.replace(key, key)
            if keyLoc is 0:
                line=line.replace(key,pirateDic.get(key))
            else: line = line.replace(key, pirateDic.get(key))
            
        print(line+randomArr())
        line = input("Enter a phrase:")
    exit()
    
#readInput()

def randomArr():
    #gives a random number and returns "arr" 30% of the time
    num = random.randrange(1,10)
    if num>3:
        return ""
    else: return ", arr."


def main():
    #createDictionary()
    readInput()
    
    
main()