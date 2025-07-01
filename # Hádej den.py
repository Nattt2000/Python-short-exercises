# Hádej den

vstupni_cisla = [1, 2, 3, 4, 5, 6, 7]
vstupni_pismena = ["p", "ú", "s", "č", "p", "s", "n"]
tyden = ('pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle')

cislo_dne = int(input("Napiš číslo dne: "))


if cislo_dne not in vstupni_cisla:
    print("Špatná vstupní hodnota!")
else:
    print("Správná vstupní hodnota!")
    den_tydne = tyden[cislo_dne - 1]
    print(den_tydne)

    prvni_pismeno = input("Napiš první písmeno: ")

    if prvni_pismeno == den_tydne[0]:
        print("Správné první písmeno")
    else:
        print("Špatné první písmeno")