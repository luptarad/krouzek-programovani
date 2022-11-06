#program v Scratch: https://scratch.mit.edu/projects/651141938

#Útok z kozmu
#Tento program používá náhodná čísla.
#Ve hře se nacházíš v kozmické lodi,
#na kterou zaútočili mimozemšťané.
#Tvůj palubní počítač určuje jejich polohu
#a vypisuje ti ji v zakódované podobě.
#Aby si trefil mimozemšťana, musíš určit jeho vzdálenost tak,
#že počítaču zadáš súčin kódů.


import random

for i in range(4):
    a = random.randint(1,20)
    b = random.randint(1,10)
    print("Kody nepritele jsou:")
    print("A=",a, "B=",b,"Strilej!")
    odpoved = int(input())
    if odpoved == a * b:
        print("Nepritel znicen")
    else:
        print("Vedle!!")
    print()
    

                  
             
