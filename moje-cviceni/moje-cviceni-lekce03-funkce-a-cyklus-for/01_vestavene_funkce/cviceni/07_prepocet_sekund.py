# Cvičení 7 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá počet sekund (třeba 3661). Přepočítej ho na hodiny,
#    minuty a sekundy a vypiš je jako 1:1:1 jediným printem.


sekundy_zadani = int(input("Zadej počet sekund:"))
hodiny = sekundy_zadani // 3600
minuty = (sekundy_zadani % 3600) // 60
sekundy = sekundy_zadani % 60

print(hodiny, minuty, sekundy, sep = ":")