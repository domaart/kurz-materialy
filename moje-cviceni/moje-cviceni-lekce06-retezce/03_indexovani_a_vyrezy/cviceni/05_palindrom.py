# Cvičení 5 – Indexování a výřezy
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na slovo a vypiš, jestli se čte stejně zepředu i pozpátku.
#    Na velikosti písmen ať nezáleží, takže "Oko" projde taky.

slovo = input("Zadej slovo: ").strip().lower()

if slovo == slovo[::-1]:
    print("Slovo se čte stejně zepředu i pozpátku.")
else:
    print("Slovo se nečte stejně zepředu i pozpátku.")