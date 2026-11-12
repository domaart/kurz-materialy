# Cvičení 1 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Projdi cyklem for čísla od 1 do 30. Vypiš jen ta, která jsou
#    dělitelná třemi nebo pěti. (Nápověda: cislo % 3 == 0)


for i in range(1,30):
    if i % 3 ==0 or i % 5 == 0:
        print(i, end=", ")