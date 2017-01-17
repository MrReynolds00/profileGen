#------------------------------
#        nameGen Module
#  Licensed under GNU License
#   Not to be sold under any
#        circumstances
#          Chris Kay
#------------------------------

import random
import textOutput

def numPicker(number):
    found = False
    while found == False:
        if number >= 2831:
            number = int(number / random.randint(5,50))
            number += 1
        else:
            found = True
    return number

def maleList():
    fFirst = open("maleFirstName.txt","r")
    firstNameList = fFirst.readlines()
    firstNameList = list(map(lambda x:x.strip(),firstNameList))
    return firstNameList

def femaleList():
    fFirst = open("femaleFirstName.txt","r")
    firstNameList = fFirst.readlines()
    firstNameList = list(map(lambda x:x.strip(),firstNameList))
    return firstNameList
    
def nameGen(number,number2,lst):
    fLast = open("surnames.txt","r")
    lastNameList = fLast.readlines()
    lastNameList = list(map(lambda x:x.strip(),lastNameList))
    firstName = lst[number]
    lastName = lastNameList[number2]
    userName = firstName[0]+lastName
    print ("Your generated name is "+firstName+" "+lastName.capitalize()+".")
    nameOutput = firstName+","+lastName.capitalize()+","+userName+","
    textOutput.writeLineAppend(nameOutput)
    f = open("savedname.txt","w")
    f.write(firstName+lastName.capitalize())
    f.close()

def generator(gender):
    ranNum = random.randint(1,10000000000000) * random.randint(1,10000)
    solvedNum = int(numPicker(ranNum))
    solvedNum2 = int(numPicker(ranNum))
    if gender == "m":
        lst = maleList()
        nameGen(solvedNum,solvedNum2,lst)
    else:
        lst = femaleList()
        nameGen(solvedNum,solvedNum2,lst)

def main(gender):
    if gender[0].lower() == "m":
        generator(gender[0].lower())
    elif gender[0].lower() == "f":
        generator(gender[0].lower())
    else:
        print ("Invalid input. Please double check your wording.")
        main(gender,counter)
