# Cvičení 9 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se uživatele na tři čísla (klidně i záporná) a vypiš,
#    jak velké je to největší z nich bez ohledu na znaménko.
#    Např. z čísel -20, 5 a 12 je největší velikost 20.

prvni_cislo = int(input("Zadej první číslo:"))
druhe_cislo = int(input("Zadej druhé číslo:"))
treti_cislo = int(input("Zadej třetí číslo:"))
print(max(abs(prvni_cislo), abs(druhe_cislo), abs(treti_cislo)))

# je lepsi vstupni cislo pri ulozeni neupravovat