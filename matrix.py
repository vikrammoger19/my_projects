from numpy import *
# arr=array([
#
#     [1,2,3,4,5,6],
#     [3,4,5,7,8,9]
# ])
# print(arr)
#
# # covert 2d into 1d array
# arr1=arr.flatten()
# print(arr1)
#
# # convert 1d into multidimensinal array
# arr2=arr.reshape(4,3)
# print(arr2)

# matrix
# convert given array into matrix
# arr_m=array([
#
#     [1,2,3],
#     [3,4,5]
# ])
# m=matrix(arr_m)
# print(m)

# matrix multiplication
m1=matrix('1,2,3;4,5,6;1,6,7')
m2=matrix('1,5,3;4,7,6;3,6,4')
print(m1+m2)
print(m1*m2)