n = 10
first = 0
second = 1

if n < 0:
    print("enter the positive number")
else:
    if n == 1:
        print(first)
    else:
        print(first)
        print(second)
        for i in range(2, n):
            result = first + second
            first = second
            second = result
            print(result)
