import random as r
punkty = [round(r.uniform(0,50),2) for i in range(15)]
print(punkty)
print(f"Najwieksza ilosc punktów: {max(punkty)} Najmniejsza ilosc punktow: {min(punkty)}")
x = float(input("Podaj liczbę: "))
if x in punkty:
    print(punkty.index(x))
else:
    print("Poza listą")
a=sum(punkty)
b=len(punkty)
srednia=round(a/b,2)
print(srednia)
ponizej=[]
for i in punkty:
    if i < srednia:
        ponizej.append(i)
print(len(ponizej), ponizej)
powyzej=[i for i in punkty if i > srednia]
print(len(powyzej), powyzej)

