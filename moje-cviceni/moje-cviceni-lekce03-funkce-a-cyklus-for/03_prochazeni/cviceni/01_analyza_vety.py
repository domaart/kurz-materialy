# Cvičení 1 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Analýza věty. Uživatel zadá větu. Projdi ji znak po znaku a vypiš
#    počet znaků, počet samohlásek, počet mezer a počet slov ve větě.
#    (Počet slov = počet mezer + 1.)


znaky = 0
samohlasky = 0
mezery = 0
veta = input("Zadej větu: ")

for i in veta:
    if i in "aeiouy":
        samohlasky = samohlasky + 1
    if i == " ":
        mezery = mezery + 1

slova = mezery + 1

print("počet znaků:", len(veta), ", počet samohlásek:", samohlasky, ", počet mezer:", mezery, ", počet slov:", slova)
    