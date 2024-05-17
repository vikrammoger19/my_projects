a = 10

print(id(a))


def fun():
    a = 8
    x = globals()['a']
    print(id(x))
    print("inside fun", a)


fun()
print("outside fun", a)
