# Cvičení 5 – Podmínky
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na počet bodů z testu (0 až 100) a vypiš známku:
#    90 a víc → 1, 75 a víc → 2, 60 a víc → 3, 40 a víc → 4,
#    jinak → 5.


pocet = int(input("Jaký počet bodů?"))

if (pocet >= 0 and pocet <=100):
    if pocet  >= 90:
        print(1)
    elif pocet >= 75:
        print(2)

    elif pocet >= 60:
        print(3)

    elif pocet >= 40:
        print(4)

    else:
        print(5)

#při tisknutí čísla ho nemusíme dávat do uvozovek