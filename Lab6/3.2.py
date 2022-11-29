def wyswietl(**kwargs):
    for x in kwargs.keys():
        print(x, kwargs[x])

wyswietl(imie="Adrian", wiek="20",nazwisko="Nowak")
