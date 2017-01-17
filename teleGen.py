#------------------------------
#        teleGen Module
#  Licensed under GNU License
#   Not to be sold under any
#        circumstances
#          Chris Kay
#------------------------------

import random
import string
import textOutput

def ranNum(size,chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def mobileNum():
    telephone = "07" + (ranNum(9))
    return telephone

def main():
    num = mobileNum()
    print ("His/Her mobile number is "+str(num)+".")
    numOut = (str(num)+",")
    textOutput.writeLineAppend(numOut)
