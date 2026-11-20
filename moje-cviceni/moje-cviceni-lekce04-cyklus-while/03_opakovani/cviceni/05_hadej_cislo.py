# Cvičení 5 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Hra "hádej číslo":
#    - Počítač si vylosuje číslo od 1 do 20: randrange(1, 21)
#    - Uživatel hádá. Po každém tipu vypiš "Moc velké." nebo "Moc malé.".
#    - Když trefí, vypiš "Trefa!" a skonči.
#    - Když se netrefí ani na pátý pokus, prozraď číslo a skonči.
#    Nahoru na první řádek nezapomeň:  from random import randrange


from random import randrange
pocet = 0
i = randrange(1, 21)


while True:
    tip = int(input("Hádej číslo od 1 do 20: "))
    pocet = pocet + 1

    if i == tip
          print("Trefa!")
          break

     if pocet == 5:
            print("Nevyšlo to ani na pátý pokus, bylo to číslo:", i)
            break

    if tip > i:
        print("Moc velké.")
    else:
        print("Moc malé.")
    

   

   