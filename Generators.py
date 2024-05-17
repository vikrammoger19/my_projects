def PowTwoGen(max=10):
    n = 0
    while n < max:
        sq=2 ** n
        yield sq
        n += 1


count = PowTwoGen()
for i in count:
    print(i)
