x = int(input("Podaj pierwsza liczbe: "))
y =int(input("Podaj druga liczbe: "))

while y>x:

    if x % 2 != 0:
        x += 1
        continue
    print(x, end=" ")
    x += 1


