# Cvičení 5 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Sleva na vstupné. Slevu mají děti (do 18 let) a senioři (65 a víc).
#    Navíc mají v pondělí slevu úplně všichni.
#    Zeptej se na věk a na den a vypiš "Máš slevu." / "Plné vstupné.".


vek = int(input("Jaký věk?"))
den = input("Jaký den?")

if (vek >= 65 and vek <18) or den == "pondělí":
    print("Máš slevu.")
else:
    print("Plné vstupné.")