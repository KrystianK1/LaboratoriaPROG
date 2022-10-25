x = int(input("Podaj pierwsza liczbe: "))
y =int(input("Podaj druga liczbe: "))
if y<x:
    x,y=y,x
while y>=x:
    print(x, end=" ")
    x = x + 1

