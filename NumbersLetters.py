#################################################################
#                                                               #
#                     Stephen Bridgett                          #                                                 
#                Numbers and Letters Analyzed                   #
#                                                               #                                                
#################################################################

from collections import Counter
import time

#benchmark function to time all of the functions
def timeFunction(f):
    startTime = time.time()
    print(f)
    endTime = time.time()
    totalTime = endTime - startTime
    return totalTime

#sum of n integers
def one(n):
    x = 0
    y = 1
    for i in range(0,n):
         x+= y
         y+= 1     
    sum = ("The sum of " + str(n) + "'s integers is " +str(x)+ ".")
    return sum

print("----------TEST ONE-----------")
print(timeFunction(one(23)))
print()
print(timeFunction(one(505)))
print()
print(timeFunction(one(10**7)))
print()

def oneone(n):
    total = (n * (n+1))/2
    sum = ("The sum of " + str(n) + "'s integers is " + str(int(total))+".")
    return sum

print(timeFunction(oneone(23)))
print()
print(timeFunction(oneone(505)))
print()
print(timeFunction(oneone(10**7)))
print()

#check if word is valid
def two(s):
    fobj = open("words.txt")
    text = fobj.read().strip().split()

    while True:
       if s in text: #string in present in the text file
            sum = ("True, '" + str(s) + "' is a valid word!")
            return sum
            break
       else: #string is absent in the text file
            sum = ("Uh oh, '" + str(s) + "' is not a valid word. Try again.")
            return sum
            break
        
print("----------TEST TWO-----------")
print(timeFunction(two("run")))
print()
print(timeFunction(two("classroom")))
print()
print(timeFunction(two("kenfkqwnfck")))
print()      

#check if word can be made from tiles
def three(word,letters):
     for words in word:
        if not Counter(word) - Counter(letters):
            sum = ("Yes, '" + str(word) + "' can be made from the letters '"
                   +str(letters) + "'!")
            return sum
            break
        else:
            sum = ("Oops, it doesn't seem like '" + str(word) +
                   "' can be made from the letters '" + str(letters)
                   +"'. Try again.")
            return sum
            break

print("---------TEST THREE----------")
print(timeFunction(three("frog", "froglkdmveowwmwwefgm")))
print()
print(timeFunction(three("classroom", "jndfwdnw")))
print()
print(timeFunction(three("run","rakfuvn")))
print()

#helper function that creates the variable containing the master list of words
def lookUp():
    readDict = open("words.txt", "r")
    master = readDict.read()
    readDict.close()
    master = master.split("\n")
    return master

wordMaster = lookUp()

#function that checks the letters against the dictionary and appends valid words to a list
def four(fRack):
    validList = []
    for item in wordMaster:
        letterBank = list(fRack)
        for letter in item:
            if letter in letterBank:
                valid = True
                letterBank.remove(letter)
            else:
                valid = False
                break
        if valid == True:
            validList.append(item)
    return validList

print("---------TEST FOUR-----------")
print("Below are words that can be created from the letters in the word 'retains':")
print()
print(timeFunction(four("retains")))
print()

#function that checks the "Speling Bee' letters against the dictionary and appends valid words to a list
def five(fRack):
    validList = []
    for item in wordMaster:
        letterBank = list(fRack)
        for letter in item:
            if letter in letterBank:
                valid = True
                letterBank.remove(letter)
            else:
                valid = False
                break
        if valid == True:
            validList.append(item)
    return validList

print("---------TEST FIVE-----------")
print("Below are words that can be created from \nthe Spelling Bee letters 'l'a'b'c'i'n'r':")
print()
print(timeFunction(five("labcinr")))
print()

#imports our text file into a list of strings
p = open("words.txt","r") 
lines = p.readlines()
myList = []
for line in lines:
    myList.append(line.split())
for i in range(len(myList)):
    myList[i] = myList[i][0]




























