#program v Scratch: https://scratch.mit.edu/projects/651101717

import random
import sys

print("Start kosmicke lodi")

#NASTAVENI
gravitace = random.randint(1, 10)
hmotnost_lode = random.randint(1, 20)
potrebna_sila_motoru = gravitace * hmotnost_lode
i = 0

print("Gravitace =", gravitace)
print("")

while i < 10:
    odpoved = int(input("Zadej silu motora:"))
    if (odpoved < potrebna_sila_motoru):
        print("Prilis malo")
    if (odpoved > potrebna_sila_motoru):
        print("Prilis moc")
    if (odpoved == potrebna_sila_motoru):
        print("Uspesny start! Jses zachranen!")
        sys.exit(0)
        
    print("Zkus to znovu")
    print("")
    print("")
    i = i + 1

print("Start se ti nepovedl")
print("Budes sezran vesmirnymi krabmi")







      
