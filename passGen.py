#------------------------------
#        passGen Module
#  Licensed under GNU License
#   Not to be sold under any
#        circumstances
#          Chris Kay
#------------------------------

import random
import string
import textOutput

def passGen(size,chars = string.ascii_letters + string.digits):
    passwrd = ''.join(random.choice(chars) for _ in range(size))
    print ("Password is "+passwrd)
    passwrd = passwrd+","
    textOutput.writeLineAppend(passwrd)
    return passwrd

def main():
    passwrd = passGen(random.randint(10,20))
    
