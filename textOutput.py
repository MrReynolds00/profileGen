#------------------------------
#      textOutput Module
#  Licensed under GNU License
#   Not to be sold under any
#        circumstances
#          Chris Kay
#------------------------------

import random

def clean():
    file = open("0output.txt","w")
    file.close()

def writeLineAppend(text):
    file = open("0output.txt","a")
    file.write(text)
    file.close()


