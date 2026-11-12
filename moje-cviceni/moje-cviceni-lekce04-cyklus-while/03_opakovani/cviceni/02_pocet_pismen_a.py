# Cvičení 2 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá slovo. Spočítej, kolikrát se v něm objeví
#    písmeno "a", a výsledek vypiš.

pocet = 0

slovo = input("Zadej slovo:")
for a in slovo:
    if a == "a":
        pocet = pocet + 1

print(f"V zadaném slově bylo písmeno \"a\" celkem {pocet}krát.")