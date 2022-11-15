# Ghost Game
# v Scratch - zadani: https://scratch.mit.edu/projects/761950068/
# v Scratch - reseni: https://scratch.mit.edu/projects/761930857/

from random import randint

print("Ghost Game")


citit_se_statecne = True
score = 0

while citit_se_statecne:
    dvere_duch = randint(1, 3)
    print("Troje dvere...")
    print("Duch je za jednimi z nich.")
    print("Ktere dvere otevres?")
    door = input("1, 2, nebo 3?")
    dvere_cislo = int(door)

    if dvere_cislo == dvere_duch:
        print("DUCH!")
        citit_se_statecne = False
    else:
        print("Zadny duch!\n")
        print("Vstupujete do dalsi mistnosti.")
        score = score + 1
print("Utikej!")
print("Game over! Tve skore:", score)
