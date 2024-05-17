# different datatypes
# 1.None
# 2.Numeric
# 3.Lists
# 4.Tuple
# 5.set
# 6.string
# 7.range
# 8.dictionary

# 1.None: It contains null values
# 2. Numeric type
# integer
a = 5
print(type(a))
# float
b = 5.2
print(type(b))
# complex type
c = 6 + 3j
print(type(c))
# Boolean
d = False
print(type(d))

# Type casting
x = 10.5
y = int(x)
print(type(y))

z = float(y)
print(type(z))

v = complex(a, b)
print(v)

# 3.Lists
my_lsi = [1, 2, 3, 5]
print(type(my_lsi))

# 4.set

s = {1, 2, 3, 5, 2}
print(type(s))

# 5
tup = (1, 2, 3, 4)
print(type(tup))

# 6.string
str = "python"
print(type(str))

# 7.range

s = range(0, 10)
print(list(s))
print(type(s))

# 8.dictionary

dict = {"samsung": "galaxy", "apple": "iphone", "mi": "redmi"}
print(type(dict))
print(dict["apple"])
print(dict.get("samsung"))
