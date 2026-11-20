# Cvičení 4 – Indexování a výřezy
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na jméno souboru a vypiš, jestli je to obrázek,
#    tedy jestli končí na .png

soubor = input("Zadej jméno souboru: ")
if soubor.strip().lower().endswith(".png"):
    print("Je to obrázek.")
else:
    print("Není to obrázek s koncovkou .png.")
