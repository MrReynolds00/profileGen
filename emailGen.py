#------------------------------
#      emailGen Module
#  Licensed under GNU License
#   Not to be sold under any
#        circumstances
#          Chris Kay
#------------------------------

import random
import textOutput
import string

def emailGen(size,chars = string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

def buildName():
    f = open("savedname.txt","r")
    name = f.read()
    f.close()
    return name

def pickSuffix():
    file = open("netsuffix.txt","r")
    suffixList = file.readlines()
    suffixList = list(map(lambda x:x.strip(),suffixList))
    number = random.randint(1,10000000000000)
    found = False
    while found == False:
        if number >= len(suffixList):
            number = int(number/ random.randint(5,20))
            number += 1
        else:
            found = True
    suffix = suffixList[number]
    return suffix    

def main():
    address = buildName()
    domain = emailGen(random.randint(1,15))
    suffix = pickSuffix()
    print ("Email is "+str(address)+"@"+domain+suffix)
    fullEmail= address+"@"+domain+suffix+","
    textOutput.writeLineAppend(fullEmail)
    
    
