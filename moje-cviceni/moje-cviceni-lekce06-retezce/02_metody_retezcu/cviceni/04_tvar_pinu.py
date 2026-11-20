# Cvičení 4 – Metody řetězců
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na PIN a zkontroluj, jestli má správný tvar: přesně čtyři
#    znaky a všechny číslice. Vypiš, jestli je v pořádku.
#    Mezery navíc ať nevadí.
#
#    V lekci 5 jsi PINu dávala tři pokusy na uhodnutí. Tady jde o to,
#    jestli vůbec vypadá jako PIN.

pin = input("Zadej PIN: ").strip()

if len(pin) == 4 and pin.isdigit():
    print(f"Pin {pin} je v pořádku.")
else:
    print(f"Pin neodpovídá požadovanému formátu.")

# nezapomínat na uvozovky na konci f string