#program v Python https://scratch.mit.edu/projects/651136532/

import random
cislo = random.randint(1,20)
odpoved = int(input("Myslim si cislo od 1 do 20. Kolik to je?"))
while odpoved != cislo:
    if odpoved < cislo:
        print("Tvoje cislo je prilis nizke")
    else:
        print("Tvoje cislo je prilis vysoke")
    odpoved = int(input("Hadej znovu:"))
print("Blahopreji! Spravna odpoved.")


                  
             
