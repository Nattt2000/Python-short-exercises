# Kámen, nůžky, papír

import random
moznosti = ['kamen', 'nuzky', 'papir']
hrac_volby = []
pocitac_volby = []

while len(hrac_volby) < 3 and len(pocitac_volby) < 3:
    hrac_pokus = random.choice(moznosti)
    hrac_volby.append(hrac_pokus)
    pocitac_pokus = random.choice(moznosti)
    pocitac_volby.append(pocitac_pokus)
#print(hrac_volby)
#print(pocitac_volby)

for i in range(3):
    if hrac_volby[i] == pocitac_volby[i]:
        vysledek = "Remíza!"
        print("Výsledek:", vysledek)
    elif hrac_volby[i] == "kamen" and pocitac_volby[i] == "nuzky":
        vysledek = "Vyhrává hráč!"
        print("Výsledek:", vysledek)
    elif hrac_volby[i] == "nuzky" and pocitac_volby[i] == "papir":
        vysledek = "Vyhrává hráč!"
        print("Výsledek:", vysledek)
    elif hrac_volby[i] == "papir" and pocitac_volby[i] == "kamen":
        vysledek = "Vyhrává hráč!"
        print("Výsledek:", vysledek)
    else:
        vysledek = "Vyhrává počítač!"
        print("Výsledek:", vysledek)
