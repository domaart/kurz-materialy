# Cvičení 3 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadává čísla tak dlouho, dokud nezadá 0. Nakonec vypiš
#    jejich součet, kolik jich bylo a jejich průměr zaokrouhlený
#    na jedno desetinné místo. (Nápověda: round(cislo, 1))


cislo = int(input("Zadej číslo: "))
soucet = 0
pocet = 0

if cislo != 0:
    while True:
        pocet = pocet + 1
        soucet = soucet + cislo
        cislo = int(input("Zadej číslo: "))
        if cislo == 0:
            break
        
    print(f"Součet čísel: {soucet}, počet: {pocet}, průměr: {round(soucet / pocet, 1)}")
else:
    print("Součet čísel, jejich počet a průměr nelze vypočítat, protože číslo jiné než nula nebylo ani jedno.")

