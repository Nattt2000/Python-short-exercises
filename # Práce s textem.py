# Práce s textem

jmeno_souboru = "muj_soubor.txt"
prvni_radek = "První řádek v souboru,\n"
druhy_radek = "druhý řádek v souboru,\n"
treti_radek = "třetí řádek v souboru."


def zapis_do_souboru(jmeno_souboru, *args):
  with open(jmeno_souboru, mode = "w", encoding = "utf-8") as soubor:
    for radek in args:
      soubor.write(radek)
zapis_do_souboru(jmeno_souboru, prvni_radek, druhy_radek, treti_radek)

def nacti_ze_souboru(jmeno_souboru):
  with open(jmeno_souboru, mode = "r", encoding = "utf-8") as soubor:
    obsah = soubor.readlines()
  return(obsah)
  
existujici_txt = nacti_ze_souboru(jmeno_souboru)
print("Jednotlivé řádky:", end=' ')
print(''.join(existujici_txt))