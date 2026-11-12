# Cvičení 6 – For versus while
# Nejdřív rozhodni for/while a napiš si do komentáře proč, pak úlohu naprogramuj.

# V nádrži je 45 litrů vody a každou minutu z ní uteče 3 litry.
#    Po každé minutě vypiš, kolik vody zbývá, a nakonec vypiš,
#    po kolika minutách je nádrž prázdná.


# while, protože nevíme kolikrát

nadrz = 46
minut = 0

while nadrz > 0:
    minut = minut + 1
    nadrz = nadrz - 3
    print(f"Uběhlo {minut} minut a v nádrži zbývá {nadrz} litrů vody.")
print("V nádrži už není voda, uběhlo celkem minut:", minut)

# Pozor ať odčítáme od aktuálního množství!
# co kdybychom upřesnili čas na vteřiny?