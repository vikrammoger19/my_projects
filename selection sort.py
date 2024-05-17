my_list = [4, 3, 1, 5, 2]
sorted_list = []

for i in range(len(my_list)):
    min = i
    for j in range(i + 1, len(my_list)):
        if my_list[j] < my_list[min]:
            temp = my_list[j]
            my_list[j] = my_list[min]
            my_list[min] = temp
for i in my_list:
    sorted_list.append(i)
print(sorted_list)
