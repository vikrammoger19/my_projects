my_list = [4, 3, 1, 5, 2]
sorted_list = []
for i in range(0, len(my_list)):
    for j in range(0, len(my_list) - 1 - i):
        if my_list[j] > my_list[j + 1]:
            temp = my_list[j]
            my_list[j] = my_list[j + 1]
            my_list[j + 1] = temp
for i in my_list:
    sorted_list.append(i)
print(sorted_list)
