# Hledej emailové adresy

zadany_text = '''\
Lorem ipsum dolor sit amet, consectetur adipiscing
elit. Mauris vulputate lacus id eros consequat tempus.
Nam viverra velit sit amet lorem lobortis, at tincidunt
tiger123@email.cz auctor massa molestie at. Nunc 
tristique fringilla congue. Donec ante diam cnn@info.com,
dapibus lacinia vulputate vitae, ullamcorper in justo.
vitae massa. Cras abc@gmail.com vel libero felis.
In augue elit, porttitor nec molestie quis, auctor
a quam. Quisque b2b@money.fr pretium dolor et tempor
luctus lacinia risus. Maecenas posuere leo sit amet
spam@info.cz. elit tincidunt maximus. Aliquam erat
volutpat. Donec eleifend felis at leo ullamcorper
fringilla est. Maecenas gravida turpis nec ultrices
aliquet.'''

import string

def je_email(slovo):
  return("@" in slovo)

def uloz_emailove_adresy(text, kontrola):
  emailove_adresy = set()
  for slovo in text.split():
    slovo_clear = slovo.strip(string.punctuation)
    if kontrola(slovo_clear) == True:
      emailove_adresy.add(slovo_clear)
  return(emailove_adresy)
  
vysledky = uloz_emailove_adresy(zadany_text, je_email)
print(f"Načtené emaily: {vysledky}")

