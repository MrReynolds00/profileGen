#------------------------------
#      Profile generator
#  Licensed under GNU License
#   Not to be sold under any
#        circumstances
#          Chris Kay
#------------------------------

import random
import streetGen
import nameGen
import passGen
import teleGen
import emailGen
import genderSelect
import textOutput

textOutput.clean()
repeat = int(input("How many profiles do you wish to generate?  "))

for x in range(0,repeat):
    gender = genderSelect.main()
    nameGen.main(gender)
    passGen.main()
    streetGen.main()
    teleGen.main()
    emailGen.main()
    print("\n")

input("Press ENTER to close... ")
 
