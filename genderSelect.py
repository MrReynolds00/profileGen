#------------------------------
#     genderSelect module
#  Licensed under GNU License
#   Not to be sold under any
#        circumstances
#          Chris Kay
#------------------------------

import random

def main():
    randomNum = random.randint(1,2)
    if randomNum == 1:
        gender = "Male"
        print("Sexy is male.")
    elif randomNum == 2:
        gender = "Female"
        print ("Sexy is female")
    else:
        main()
    return gender
