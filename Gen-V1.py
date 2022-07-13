from bdb import GENERATOR_AND_COROUTINE_FLAGS
import random 
import string
import os
import time
from typing_extensions import Self, Type
from xml.dom.pulldom import CHARACTERS

from numpy import character
# ^^ Modlues to make the scirp run the script correctly.

#after importing all the modules needed start typeing the sctipt.

#(optinal) select the output folder/file.
output_file = "Output.txt"
#now the script.
#(optional) you can use ascii text art to add a lil bit of spice to your code.
print("  #####  ####### #     #       #     #   # ") 
time.sleep(0.2)
print(" #     # #       ##    #       #     #  ##   ")
time.sleep(0.2)
print(" #       #       # #   #       #     # # #   ")
time.sleep(0.2)
print(" #  #### #####   #  #  # ##### #     #   #   ")
time.sleep(0.2)
print(" #     # #       #   # #        #   #    #   ")
time.sleep(0.2)
print(" #     # #       #    ##         # #     #   ")
time.sleep(0.2)
print("  #####  ####### #     #          #    ##### ")

print("NOTE:PLEASE DONT PUT A HUGE NUMBER IN ANY OF THE FIELDS BECAUSE THE TOOL CANNOT HANDLE IT. (MAX IS 10B)")
#time.sleep to print the next line in a longer time.
time.sleep(3)

print("\nMADE BY BAIBERS")
time.sleep(1)
#amount to chose how many (anything) wanted to be printed.
amount = int(input("\nstrings:"))
#character_amount to chose how many characters in each string will be generated.
character_amount = int(input("characters:"))
for i in range (amount):
        generated = ("").join(random.choices(string.ascii_letters + string.digits, k = character_amount))  
        print("[*]", generated, "\n")
        with open (output_file, "a") as f:
            f.write(generated + "\n")
            
            #input("anything you want") should stop thew script from closing automaticly.
print("Generating done successully! Check the output file.")
time.sleep(0.5)
input("Press enter to close the program.")
#after that we run the script and it should run correcly and it should generate the strings and characters you want!