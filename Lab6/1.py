def z1(imie, wiek=20):
    '''
    Funkcja zwraca wartości imię i wiek.
    :param imie:
    :param wiek:
    :return:
    '''
    print(imie, wiek)

z1("Marcin", 25)
z1("Marek", 30)
z1(wiek=20, imie="Piotr")
print(z1.__doc__)
z1("Piotr",)

