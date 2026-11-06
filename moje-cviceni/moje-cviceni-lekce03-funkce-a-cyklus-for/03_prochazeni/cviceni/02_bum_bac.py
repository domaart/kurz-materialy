# Cvičení 2 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Bum-Bác. Tuhle úlohu znáš z minula pro jedno číslo – teď ji necháme
#    proběhnout cyklem. Vypiš čísla od 1 do 30, ale:
#    - za dělitelné třemi i pěti zároveň vypiš "BumBác",
#    - za dělitelné jen třemi vypiš "Bum",
#    - za dělitelné jen pěti vypiš "Bác",
#    - jinak vypiš samotné číslo.


for i in range(1,31):
    if i % 15 == 0:
        print(i, "BumBác")
    elif i % 3 == 0:
            print(i, "Bum")
    elif i % 5 == 0:
                print(i, "Bác")
    else:
        print(i)

# dělitelné 3 i 5 = dělitelné 15, musí být první