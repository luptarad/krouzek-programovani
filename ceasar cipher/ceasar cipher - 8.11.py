zprava = input("Zadej zpravu pro zasifrovani")
heslo = int(input("Zadej tajne cislo"))

abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
sifrovana = "" #na zacatku prazdna zasifrovana zprava

zprava = zprava.upper()

for aktualni_pismeno in zprava: #cyklus pro kazde pismenko ve zprave
    pozice = abeceda.find(aktualni_pismeno)
    nova_pozice = pozice + heslo
    sifrovana = sifrovana + abeceda[nova_pozice]
    

print(zprava)
print(heslo)
print(sifrovana)

