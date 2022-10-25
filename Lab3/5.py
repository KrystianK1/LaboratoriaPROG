n =int(input("Podaj liczbe studentów: "))
i = 1
suma = 0
while i <= n:
    punkty = input(f"Podaj punkty {i}: ")
    suma += punkty
    i += 1
srednia = suma / n
print(f"Średnia liczba punktow: {srednia}:")