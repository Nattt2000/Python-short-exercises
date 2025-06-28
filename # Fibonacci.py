# Fibonacci

x = 0
y = 1
vysledky = []
delka_rady = 15
vysledky.append(x)
vysledky.append(y)

while len(vysledky) < delka_rady:
  mezisoucet = x + y
  vysledky.append(mezisoucet)
  x = y
  y = mezisoucet
print(f"Fibonacci: {vysledky}")
  