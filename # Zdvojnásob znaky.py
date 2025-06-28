# Zdvojnásob znaky

import string
vstupni_text = "Ahoj všem, tady Engeto"

def zdvojnasob_znaky(vstupni_text):

  slova = vstupni_text.split()

  vsechna_pismena = []
  for slovo in slova:
      *pismena, = slovo
      vsechna_pismena.extend(pismena)

  zdvojene = []
  for pismeno in vsechna_pismena:
      zdvojene_pismeno = pismeno * 2
      zdvojene.append(zdvojene_pismeno)
      spojene = "".join(zdvojene)
      smezerou = spojene[:8] + "  " + spojene[8:18] + "  " + spojene[18:26] + "  " + spojene[26:]
  return(smezerou)

vysledek = zdvojnasob_znaky(vstupni_text)
print("Zdvojené znaky:", vysledek)

