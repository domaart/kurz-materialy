# Cvičení 8 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Zboží stojí 1000 Kč bez DPH. Na jeden řádek vypiš cenu bez DPH
#    i s DPH (21 %). Použij dva printy – první nech řádek pokračovat,
#    druhý ho dokonči.
cena = 1000
cena_s_dph = cena * 1.21

print("Cena v Kč bez DPH:", cena, end=", ")
print("cena v Kč s DPH:", round(cena_s_dph))

#v kodu je treba pouzivat desetinnout tecku misto carky