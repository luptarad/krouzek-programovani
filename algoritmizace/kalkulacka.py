def scitej():
    print("Soucet je:", cislo1 + cislo2)

def vynasob():
    print("Nasobek je:", cislo1 * cislo2)

cislo1 = int(input("Kamo, zadej cislo"))
cislo2 = int(input("Kamo, jeste jedno"))

volba = input("Scitat[s] nebo nasobit [n]?")

if volba == "s":
    scitej()    
elif volba == "n":
    vynasob()
else:
    print("Rozhodni se, co chces")

    
    


