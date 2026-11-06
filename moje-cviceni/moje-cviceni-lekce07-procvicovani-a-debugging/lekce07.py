#PTM add conditional breakpoint (break when expression evaluates to true, např. si nastavím 100), 

for i in range(0, 10001):
    if i == 1000:
        print(f"Ahoj {i}")
    else:
        print("Není tisíc")