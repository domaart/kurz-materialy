# Cvičení 1 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Platný trojúhelník. Ze tří stran jde sestavit trojúhelník jen tehdy,
#    když je součet každých dvou stran větší než ta třetí.
#    Vypiš "Platný trojúhelník." / "Takový trojúhelník nejde.".
a = 3
b = 4
c = 5


if a + b > 3 and b + c > a and c + a > b:
    print("Platný trojúhelník.")
else:
    print("Takový trojúhelník nejde.")