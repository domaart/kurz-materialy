# Cvičení 3 – Metody řetězců
# Doplň kód pod zadání a soubor spusť (Run).

# Ptej se na velikost trička, dokud uživatelka nenapíše S, M nebo L.
#    Na nic jiného se nespokoj a zeptej se znovu. Velikost písmen
#    ani mezery navíc ať nevadí – "s" i "  M  " mají projít.
#    Nakonec vypiš objednanou velikost velkým písmenem.
#
#    Cyklus while True a break znáš z lekce 4.

velikost = "nezadána"

while True:
    velikost = input("Zadej velikost trička (S/M/L): ").strip().upper()
    if velikost == "S" or velikost == "M" or velikost == "L":
        print("Objednaná velikost je:", velikost)
        break
    else:
        continue

# jde to udělat vyhledáváním in slovo