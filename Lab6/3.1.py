'''def wyswietl(*args):
    print(args)
    n=args[0]
    for i in args[1:]:
        if i>n:
            n=i
    return n



print(wyswietl(20,3,1.4))

print(wyswietl(1,2,1.4))
a=(wyswietl(5,7,1.4))
print(a)'''


def wyswietl(num1,*args):
    n=num1
    for i in args:
        if i>n:
            n=i
    return n
print(wyswietl("aha", ))
