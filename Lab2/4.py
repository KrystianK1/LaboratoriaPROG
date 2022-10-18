print("""Jaką operację chcesz wykonać?
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie""")

operacja=(input("wpisz numer operacji: "))
x = float(input("Podaj argument 1: "))
y = float(input("Podaj argument 2: "))
if operacja==1:
    z=(f"{x}+{y}={x+y}")
elif operacja==2:
    z = (f"{x}-{y}={x - y}")
elif operacja==3:
    z = (f"{x}*{y}={x * y}")
elif operacja==4:
    z = (f"{x}//{y}={x // y}")
elif operacja==5:
    z = (f"{x}**{y}={x ** y}")
else:
    print("niepoprawna operacja")
print(z)





numer=input("Podaj numer operacji: ")
