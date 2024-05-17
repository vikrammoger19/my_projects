# Decorator is used to add extra features to the existing functions.
# Modifies the functionality of function by wrapping it in another function.
def add(x, y):
    return x + y


def calculate(func, x, y):
    return func(x, y)


result = calculate(add, 4, 6)
print(result)  # prints 10
