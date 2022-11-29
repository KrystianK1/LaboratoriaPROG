def wyswietl(*args):
    print(args)
    for i in args:
        print(i, end=' ')
    print()



wyswietl(1,3,"abc",1.4,[1,2,3])
wyswietl(1,2,"asdfa",1.4,[1,25,33])
wyswietl()