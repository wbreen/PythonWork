# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 13:35:54 2017

@author: William Breen
"""
import re


def main():
    #To run listComps, uncomment it, it should print out the answer number then the answer
    #listComps()
    #Put the name of the file in the parameters of readFileToList, don't necessarily need '.txt' on end
    #myList = readToList("Military_Alphabet.txt")
    myList = readToList("lowerwords.txt")
    #print(myList)
    #filterList(Regex expression here, myList)
    regExpressions(myList)
    
    
# When run, this method should print out all the answers to part 1 
def listComps():
    firstSentence = ['I', 'am', 'playing', 'xbox', 'and', 'trying', 'hard']
    secondSentence = ['I', 'am', 'trying', 'hard', 'for', 'a', 'win']
    
    #Answers to questions start here
    answer1 = [x for x in firstSentence + secondSentence if len(x)>2]
    print("Answer 1:", answer1)
    
    answer2 = [x for x in firstSentence if x[0] is 'a']
    print("Answer 2:", answer2)
    
    answer3 = [x[-2:] for x in firstSentence]
    print("Answer 3:", answer3)
    
    answer4 = [x for x in firstSentence + secondSentence if len(x) % 2 is 0]
    print("Answer 4:", answer4)
    
    answer5 = [firstSentence.index(x) for x in firstSentence if len(x) %2 is 0]
    print("Answer 5:", answer5)
    
    answer6 = [x for x in firstSentence + secondSentence if x.endswith('ing')]
    print("Answer 6:", answer6)
    
    answer7 = [firstSentence[x] for x in range(0, len(firstSentence)) if firstSentence[x] == secondSentence[x]]
    print("Answer 7:", answer7)
    
    answer8 = [x for x in firstSentence for y in secondSentence if x==y]
    print("Answer 8:", answer8)
    
    answer9 = [x[0].upper()+x[1:].lower() for x in firstSentence]
    print("Answer 9:", answer9)
    
    answer10 = [x.replace('a','ee') for x in firstSentence]
    print("Answer 10:", answer10)
    
    answer11 = [(firstSentence[x], secondSentence[x]) for x in range(0,len(firstSentence)) if firstSentence[x]!=secondSentence[x]]
    print("Answer 11:", answer11)
    
    answer12 = [(firstSentence[x], secondSentence[y]) for x in range(len(firstSentence)) for y in range(len(secondSentence)) if firstSentence[x]==secondSentence[y]]
    print("Answer 12:", answer12)
    
    answer13 = [(firstSentence[x]+secondSentence[y]) for x in range(len(firstSentence)) for y in range(len(secondSentence)) if len(firstSentence[x])<len(secondSentence[y])]
    print("Answer 13:", answer13)
    
    answer14 = [x for x in range(len(firstSentence)) for y in range(len(secondSentence)) if firstSentence[x]==secondSentence[y]]
    print("Answer 14:", answer14)
    
    answer15 = [(x[0], y[0]) for x in firstSentence for y in secondSentence]
    print("Answer 15:", answer15)
    
    

#filters the list based on the regex entered using the list
def filterList(regEx, strList):
    afterFilter = [x for x in strList if re.search(regEx, x)]
    #Alternate could be:
    #afterFilter = [x for x in strList if re.regEx ,x)]
    #print(afterFilter)
    return afterFilter
  

#reads the given file to a list
def readToList(file):
    #file = "lowerwords.txt"
    correctEnd = ".txt"
    
    if file[-4:] != correctEnd :
        file += ".txt"
    newFile = open(file, 'r')
    wordList = []
    
    for line in newFile:
        line = line.split()
        for word in line:
            wordList.append(word)
    
    return wordList

def regExpressions(listName):
    #Return/print out the actual number, not the list of stuff 
    reg1 = re.compile("a$")
    list1 = filterList(reg1, listName)
    print("Answer 1:", len(list1))
    
    reg2 = re.compile("[*{4}]d$", re.M)
    list2 = filterList(reg2, listName)
    print("Answer 2:", list2)

    
main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

            