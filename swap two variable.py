a = 20
b = 10

a, b = b, a
print(a, b)

# By using third variable

temp = a
a = b
b = temp
print(a, b)

# without using third variable

a = a + b
b = a - b
a = a - b
print(a, b)
