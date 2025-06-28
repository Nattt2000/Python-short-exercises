# Slovníkový vyhledávač

zadany_slovnik = {
   'jmeno':'Pepa',
   'prijmeni': 'Novak',
   'rok_narozeni': 1990,
   'email': 'pepa.novak@seznam.cz'
}

def obsahuje_udaje(klic, hodnota, slovnik):
  try:
    slovnik[klic] == hodnota
  except KeyError:
    vysledek = False
    print(f"Klíč: {klic} nenalezen.")
  else:
    print(f"Klíč: {klic} nalezen.")
    if slovnik.get(klic) == hodnota:
      vysledek = True
    else:
      vysledek = False
      print(f"Hodnota: {hodnota} nenalezena.")
  return(vysledek)

vystup_1 = (obsahuje_udaje("jmeno", "Pepa", zadany_slovnik))
vystup_2 = (obsahuje_udaje("jmeno", "Marek", zadany_slovnik))
vystup_3 = (obsahuje_udaje("name", "John", zadany_slovnik))

print(vystup_1)
print(vystup_2)
print(vystup_3)
