# Cvičení 5 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Hody dvěma kostkami. Vnořenými cykly vypiš všechny možné hody
#    dvěma kostkami (každá má čísla 1 až 6) a u každého i jejich součet.
#    Každý řádek bude vypadat třeba takhle: 2 + 5 = 7


for a in range(1, 7):
    for b in range(1, 7):
        print(a, "+", b, "=", a + b)
