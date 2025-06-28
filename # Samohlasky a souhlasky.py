# samohlasky a souhlasky

samohlasky = 'aeiouáéíóú'
souhlasky = 'bcčdďfghjklmnňprřsštťvzžcdž'
vysledky = {'souhlasky': 0, 'samohlasky': 0}
veta = 'Zvuk řeči je produkován otevřenou konfigurací vokálního traktu'

for znak in veta:
  if znak == " ":
    continue
  elif znak in samohlasky:
    vysledky["samohlasky"] += 1
  elif znak in souhlasky or znak in souhlasky.upper():
    vysledky["souhlasky"] += 1

print(f"Počet souhlásek: {vysledky['souhlasky']} | Počet samohlásek: {vysledky['samohlasky']}")
