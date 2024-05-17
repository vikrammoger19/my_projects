# n = 5
# fact = 1
# for i in range(1, n + 1):
#     fact = fact * i
# print(fact)
#
#
# # by using functions
#
# def fact(n):
#     count = 1
#     for i in range(1, n + 1):
#         count = count * i
#     return count
#
#
# print(fact(5))


# by using recursion

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))
