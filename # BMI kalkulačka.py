# BMI kalkulačka

import string

vyska = float(input("vyska v metrech: "))
vaha = float(input("vaha v kg: "))
jmeno = input("jmeno: ")

bmi = vaha / (vyska**2)

if bmi < 18.5:
  kategorie = "podvýživa"
elif bmi > 18.5 and bmi < 24:
  kategorie = "Zdavá váha"
elif bmi > 25 and bmi < 29:
  kategorie = "Mírná nadváha"
elif bmi > 30 and bmi < 39:
  kategorie = "Obezita"
else:
  kategorie = "Těžká obezita"

print(f"Jméno: {jmeno}, kategorie: {kategorie}")

