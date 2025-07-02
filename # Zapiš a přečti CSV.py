# Zapiš a přečti CSV

import csv

zadane_hodnoty = [
    [10, "a1", 1],
    [12, "a2", 3],
    [14, "a3", 5],
    [16, "a4", 7],
    [18, "a5", 9]
]

jmeno_souboru = "muj_soubor.csv"

def zapis_csv(jmeno, hodnoty):
    with open(jmeno, mode="w", newline="") as soubor:
        zapisovac = csv.writer(soubor, delimiter=";")
        zapisovac.writerows(hodnoty)

def precti_csv(jmeno):
    with open(jmeno, mode="r", newline="") as soubor:
        cteni = csv.reader(soubor, delimiter=";")
        return tuple(cteni)

zapis_csv(jmeno_souboru, zadane_hodnoty)
vystup = precti_csv(jmeno_souboru)

print(f"Obsah: {vystup}")
