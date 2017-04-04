# -*- coding: utf-8 -*-
"""
William Breen
Programming languages quiz 2
"""

testOne = {'x':1, 'y':2, 'z':3}
testTwo = {'x':1, 'y':2, 'z':2}

def invertDictionary(oldDict):
    invertedDic = {}
    for key in oldDict:
        newKey = oldDict[key]
        newVals = key
        if newKey in invertedDic:
            inDicVals = invertedDic[newKey]
            inDicVals.append(newVals)
            invertedDic[newKey] = inDicVals
        else:invertedDic[newKey] = [newVals]
       
    return invertedDic

print(invertDictionary(testOne))
print(invertDictionary(testTwo))

def fileAndWords():
    givenFile = input("Enter a file name:")
    print(givenFile)
    #import file to list
    wordAfter = input("Enter a word:")
    
    for word in givenFile:
        output.append(givenFileList[word+1])
        
    return output
    
fileAndWords()