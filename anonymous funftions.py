from functools import reduce


# def mul(a, b):
#     return a * b
#
#
# print(mul(5, 6))

f = lambda a, b: a * b
result = f(5, 6)
print(result)

# filter functions

my_list = [1, 2, 3, 4, 5, 6, 7, 8]

fil = list(filter(lambda n: n % 2 == 0, my_list))
print(fil)

# map functions

mul = list(map(lambda n: n * 2, fil))
print(mul)

# reduce functions

sum1 = reduce(lambda x, y: x + y, mul)
print(sum1)
