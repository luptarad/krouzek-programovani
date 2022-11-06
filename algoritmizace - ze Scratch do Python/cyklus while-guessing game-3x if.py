#program v Scratch: https://scratch.mit.edu/projects/651136532/editor/

import random

print("myslim si cislo.")
tajneCislo = random.randint(0,10)
odpoved = 0 

while (odpoved != tajneCislo):
    odpoved = int(input("hadej"))
    if(odpoved > tajneCislo):
        print("prilis velke")
    if(odpoved < tajneCislo):
        print("prilis male")
    if(odpoved == tajneCislo):
        print("spravna odpoved")
  


