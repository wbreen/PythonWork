# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 13:35:54 2017

@author: William Breen
@copyright: William Breen 2017
"""
import re


def main():
    #To run listComps, uncomment it, it should print out the answer number then the answer to the question
    listComps()
    #Put the name of the file in the parameters of readFileToList
    myList = readToList("lowerwords.txt")
    #print(myList)
    #filterList(Regex expression, myList)
    #Regular expression should be in a variable that is in the form: re.compile(r'regex')
    #regExpressions takes a list and prints the quesiton number and the results for each question for the given list
    regExpressions(myList)
    
    
# When run, this method should print out all the answers to part 1 
def listComps():
    firstSentence = ['I', 'am', 'playing', 'xbox', 'and', 'trying', 'hard']
    secondSentence = ['I', 'am', 'trying', 'hard', 'for', 'a', 'win']
    
    #Answers to questions start here
    answer1 = [x for x in firstSentence + secondSentence if len(x)>2]
    print("List Comp answer 1:", answer1)
    
    answer2 = [x for x in firstSentence if x[0] is 'a']
    print("List Comp answer 2:", answer2)
    
    answer3 = [x[-2:] for x in firstSentence]
    print("List Comp answer 3:", answer3)
    
    answer4 = [x for x in firstSentence + secondSentence if len(x) % 2 is 0]
    print("List Comp answer 4:", answer4)
    
    answer5 = [firstSentence.index(x) for x in firstSentence if len(x) %2 is 0]
    print("List Comp answer 5:", answer5)
    
    answer6 = [x for x in firstSentence + secondSentence if x.endswith('ing')]
    print("List Comp answer 6:", answer6)
    
    answer7 = [firstSentence[x] for x in range(0, len(firstSentence)) if firstSentence[x] == secondSentence[x]]
    print("List Comp answer 7:", answer7)
    
    answer8 = [x for x in firstSentence for y in secondSentence if x==y]
    print("List Comp answer 8:", answer8)
    
    answer9 = [x[0].upper()+x[1:].lower() for x in firstSentence]
    print("List Comp answer 9:", answer9)
    
    answer10 = [x.replace('a','ee') for x in firstSentence]
    print("List Comp answer 10:", answer10)
    
    answer11 = [(firstSentence[x], secondSentence[x]) for x in range(0,len(firstSentence)) if firstSentence[x]!=secondSentence[x]]
    print("List Comp answer 11:", answer11)
    
    answer12 = [(firstSentence[x], secondSentence[y]) for x in range(len(firstSentence)) for y in range(len(secondSentence)) if firstSentence[x]==secondSentence[y]]
    print("List Comp answer 12:", answer12)
    
    answer13 = [(firstSentence[x]+secondSentence[y]) for x in range(len(firstSentence)) for y in range(len(secondSentence)) if len(firstSentence[x])<len(secondSentence[y])]
    print("List Comp answer 13:", answer13)
    
    answer14 = [x for x in range(len(firstSentence)) for y in range(len(secondSentence)) if firstSentence[x]==secondSentence[y]]
    print("List Comp answer 14:", answer14)
    
    answer15 = [(x[0], y[0]) for x in firstSentence for y in secondSentence]
    print("List Comp answer 15:", answer15)
    
    

#filters the list based on the regex entered using the list
def filterList(regEx, strList):
    return [x for x in strList if re.search(regEx, x)]
  

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
    reg1 = re.compile(r'a$')
    list1 = filterList(reg1, listName)
    print("Regular Expressions answer 1:", len(list1))
    
    reg2 = re.compile(r'^.{4}d$')
    list2 = filterList(reg2, listName)
    print("Regular Expressions answer 2:", len(list2))
    
    reg3 = re.compile(r'.[aeiou]$')
    list3 = filterList (reg3, listName)
    print("Regular Expressions answer 3:", len(list3))
    
    reg4 = re.compile(r'^[aeiou].*[aeiou]$', re.I)
    list4 = filterList(reg4, listName)
    print("Regular Expressions answer 4:", len(list4))
    
    reg5 = re.compile(r'^([aeiou]).*\1$', re.I)
    list5 = filterList(reg5, listName)
    print("Regular Expressions answer 5:", len(list5))
    
    reg6 = re.compile(r'.*[aeiou]{4}.*')
    list6 = filterList(reg6, listName)
    print("Regular Expressions answer 6:", len(list6))
    
    reg7 = re.compile(r'(in.*){3}')
    list7 = filterList(reg7, listName)
    print("Regular Expressions answer 7:", len(list7))
    
    reg8 = re.compile(r'([a-z][a-z]).*\1.*\1.*')
    list8 = filterList(reg8, listName)
    print("Regular Expressions answer 8:", len(list8))
    
    reg9 = re.compile(r'(([a-z])([a-z])).*\3.*\2.*\1')
    list9 = filterList(reg9, listName)
    print("Regular Expressions answer 9:", len(list9))
    
    reg10 = re.compile(r'([a-z])\1.*([a-z])\2.*([a-z])\3')
    list10 = filterList(reg10, listName)
    print("Regular Expressions answer 10:", len(list10))
    
    reg11 = re.compile(r'(([a-z])([a-z])\2).*\1')
    list11 = filterList(reg11, listName)
    print("Regular Expressions answer 11:", len(list11))
    
    reg12 = re.compile(r'(([a-z])([a-z])\2){3}')
    list12 = filterList(reg12, listName)
    print("Regular Expressions answer 12:", len(list12))
    

    
main()
    

    