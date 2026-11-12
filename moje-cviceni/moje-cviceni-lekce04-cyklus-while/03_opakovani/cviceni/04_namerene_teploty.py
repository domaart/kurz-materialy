# Cvičení 4 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadává naměřené teploty. Po každé se zeptej
#    "Další? (ano/ne) ". Až odpoví "ne", vypiš nejvyšší teplotu.

max = int(input("Zadej teplotu: "))

while True:
    dalsi = input("Chceš zadat další? ano/ne ")
    if dalsi == "ne":
        break
    teplota = int(input("Zadej teplotu: "))
    if teplota > max:
        max = teplota

print("Maximální zadaná teplota:", max)

# pozor na rozdil meze == a =
# pozor, aby byl text while "ano" v uvozovkáchf