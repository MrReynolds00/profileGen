#------------------------------
#       streetGen Module
#  Licensed under GNU License
#   Not to be sold under any
#        circumstances
#          Chris Kay
#------------------------------

import random
import textOutput

def strFirstName():
    file = open("allstreets.txt","r")
    strFirstName = file.readlines()
    strFirstName = list(map(lambda x:x.strip(),strFirstName))
    return strFirstName
    
def strLastName():
    file = open("streetlastname.txt","r")
    strLastName = file.readlines()
    strLastName = list(map(lambda x:x.strip(),strLastName))
    return strLastName

def streetNameNum(strNameList,number):
    found = False
    while found == False:
        if number >= len(strNameList):
            number = int(number/ random.randint(5,20))
            number += 1
        else:
            found = True
    return number

def displayStreetName(strFirstNum,strLastNum,strFirstList,strLastList):
    strFirstName = strFirstList[int(strFirstNum)]
    strLastName = strLastList[int(strLastNum)]
    num = str(random.randint(1,4000))
    street = num+","+strFirstName+" "+strLastName.capitalize()+","
    print ("Your address is "+num+" "+strFirstName+" "+strLastName+".")
    textOutput.writeLineAppend(street)

def main():
    number = random.randint(1,10000000000000) * random.randint(1,10000)
    firstList = strFirstName()
    lastList = strLastName()
    num1 = streetNameNum(firstList,number)
    num2 = streetNameNum(lastList,number)
    displayStreetName(num1,num2,firstList,lastList)       
    
    
