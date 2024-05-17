from array import array

from numpy import *

# 1.Array method
# arr = array([1, 2, 3, 4], float)
# print(arr.dtype)
# print(arr)
#
# # 2.lin space method
#
# arr1 = linspace(1, 15, 16)
# print(arr1)
#
# # 3.arrange method
#
# arr2 = arange(1, 15, 2)
# print(arr2)
#
# # 4.logspace method
#
# arr4 = logspace(1, 20, 10)
# print(arr4)
#
# # zeros method
# arr5 = zeros(5)
# print(arr5)
#
# # ones method
# arr6 = ones(5)
# print(arr6)


# operations on array
# arra=array([1,2,3,4,5])
# arra=arra+5
# print(arra)
# arr1=[5,6,7,9,10]
# print(arra+arr1)
#
# print(arra*arr1)
#
# print(log(arra))
# print(sqrt(arra))
# print(sum(arra))
# print(max(arra))
# print(min(arra))
# print(sort(arra))

# copy the array

my_array=array([1,2,3,4,5])
# my_array1=my_array
# print(my_array)
# print(my_array1)
# print(id(my_array))
# print(id(my_array1))

# view : if we use the view function the value of the array will be same and it will stored in two different addresses
# my_array2=my_array.view()
# print(my_array2)
# print(my_array)
# print(id(my_array))
# print(id(my_array2))

# shallow copy
# my_array2=my_array.view()
# my_array2[1]=8
# print(my_array2)
# print(my_array)
# print(id(my_array))
# print(id(my_array2))

# deep copy
my_array2=my_array.copy()
my_array[1]=8
print(my_array2)
print(my_array)
print(id(my_array))
print(id(my_array2))