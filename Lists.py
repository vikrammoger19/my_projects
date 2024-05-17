# To creating Integer List
my_list = [1, 2, 3, 4, 5]

# To creating String List
my_list1 = ["vikram", "sumant", "guru"]

# Print the list values
print(my_list1)
print(my_list)

sum_list = [my_list, my_list1]
print(sum_list)

# merging two lists
merge_list = my_list + my_list1
print(merge_list)

# to find length of the list
print(len(merge_list))

# list slicing
print(my_list[1:2])
print(my_list[3:])
print(my_list[-1])
print(my_list[:5])

# List Methods

# 1.append
my_list.append(8)
print(my_list)

# 2. insert: Inserting the element in the given index

my_list.insert(2, 9)
print(my_list)

# 3.remove:removes the given element from the list

my_list.remove(5)
print(my_list)

# 4.pop:removing the given index element
# if didn't mention the index it will remove the last element in the list
my_list.pop(3)
print(my_list)

my_list.pop()
print(my_list)

del my_list[2:]
print(my_list)

my_list.extend([5, 3, 6, 8])
print(my_list)
