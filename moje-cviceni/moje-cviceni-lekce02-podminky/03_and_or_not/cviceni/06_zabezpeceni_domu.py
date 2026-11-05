# Cvičení 6 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Zabezpečení domu. Dům je zabezpečený, jen když jsou zavřené dveře,
#    zavřená okna a zároveň zapnutý alarm.
#    Zeptej se na všechny tři věci (ano/ne). Pomocí not (…) vypiš
#    "Pozor, dům není zabezpečený!", když zabezpečený NENÍ,
#    jinak vypiš "Zabezpečeno.".


dvere = input("Jsou zabezpečené dveře? ano/ne")
okna = input("Jsou zavřená okna? ano/ne")
alarm = input("Je zapnutý alarm? ano/ne")

if not (dvere == "ano" or okna == "ano" or alarm == "ano"):
    print("Pozor, dům není zabezpečený!")
else:
    print("Zabezpečeno.")
