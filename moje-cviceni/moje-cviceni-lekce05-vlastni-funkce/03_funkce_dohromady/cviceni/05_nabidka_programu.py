# Cvičení 5 – Funkce dohromady
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš program, který pořád dokola nabízí tři možnosti a zeptá se,
#    co má udělat:
#
#      1 - hodit kostkou
#      2 - pozdravit
#      3 - konec
#
#    Volba 1 hodí kostkou a vypíše, co padlo. Volba 2 se zeptá na jméno
#    a pozdraví ho. Volba 3 program ukončí. Po volbě 1 a 2 se nabídka
#    objeví znovu. Na cokoli jiného program odpoví, že volbu nezná.
#    Použij cyklus while True.
#    Zobrazení nabídky i obě akce napiš jako vlastní funkce.

from random import randrange

def hod_kostkou():
    print(f"Na kostce padlo číslo: {randrange(1,7)}.")

def pozdrav(jmeno):
    print(f"Zdravím, {jmeno}!")

def vyber():
    print("""
Co cheš udělat?
1 - hodit kostkou
2 - pozdravit
3 - konec
    """)

def co_delat():
    while True:
        vyber()
        cinnost = input("Zadej tvůj výběr: ")
        if cinnost == "1":
            hod_kostkou()
        elif cinnost == "2":
            jmeno = input("Koho pozdravit? ")
            pozdrav(jmeno)
        elif cinnost == "3":
            print("Ukončuji.")
            break
        else:
            print("Takovou volbu neznám.")

co_delat()

# zopakovat, co dělá return nebo continue nebo break
# randrange se importuje v programu, ne ve funkci???