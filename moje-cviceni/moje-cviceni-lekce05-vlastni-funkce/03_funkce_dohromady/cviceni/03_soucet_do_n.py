# Cvičení 3 – Funkce dohromady
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci soucet_do(n), která vrátí součet čísel od 1 do n.
#    soucet_do(5) vrátí 15.


def soucet_do(n):
    soucet = 0
    for i in range(n, 0, -1):
        soucet = soucet + i
    return soucet

print("Součet do 5:", soucet_do(5))

# for cislo in range(1, n + 1):