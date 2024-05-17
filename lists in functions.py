def count(my_list):
    even = 0
    odd = 0
    for i in my_list:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even, odd = count(my_list)
print(f"even: {even} and odd:{odd}")
