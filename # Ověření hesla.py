# ověření hesla

import string

uzivatel = {"Marek": "1234"}
jmeno = input("Zadej jméno: ")
heslo = input("Zadej heslo: ")

if jmeno  in uzivatel and uzivatel[jmeno] == heslo:
  zprava = f"Ahoj {jmeno}, vítej v aplikaci! Pokračuj..."
else:
  zprava = "Uživatelské jméno nebo heslo nejsou v pořádku!"
print("Výstup:", zprava)
 