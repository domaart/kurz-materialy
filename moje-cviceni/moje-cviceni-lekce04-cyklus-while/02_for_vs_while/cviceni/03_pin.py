# Cvičení 3 – For versus while
# Nejdřív rozhodni for/while a napiš si do komentáře proč, pak úlohu naprogramuj.

# Ptej se na PIN tak dlouho, dokud uživatel nezadá "1234".
#    Pak vypiš "Odemčeno!".

# neznáme počet opakování → while

while True:
    pin = input("Zadej PIN:")
    if pin == "1234":
        print("Odemčeno!")
        break
    else:
        print("Špatný PIN.")
