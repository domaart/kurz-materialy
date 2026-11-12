# Cvičení 6 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Ptej se na heslo. Když uživatel zadá "pyladies", vypiš "Vítej!"
#    a skonči. Když se splete třikrát, vypiš "Zablokováno." a skonči taky.
#    Z cyklu se v obou případech dostaneš příkazem break.

pocet = 0
while True:
    heslo = input("Zadej heslo: ")
    pocet = pocet + 1
    if heslo == "pyladies":
        print("Vítej! Tolikrát ses zkusil přihlásit:",pocet)
        break
    if pocet == 3:
        print("Zablokováno.")
        break
    

 
