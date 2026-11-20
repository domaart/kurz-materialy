# Cvičení 1 – Indexování a výřezy
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na jméno a na příjmení a vypiš iniciály velkými písmeny.
#    Pro Annu Novákovou vyjde:  A. N.

jmeno = input("Zadej jméno: ")
prijmeni = input("Zadej příjmení: ")

print(jmeno[0].title() + ".", prijmeni[0].title() + ".")
print(f"{jmeno[0].upper()}. {prijmeni[0].upper()}.")