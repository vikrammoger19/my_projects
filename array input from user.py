from array import *


vals = array("i", [])
num = int(input("enter the number of elements u want to insert: "))
for i in range(num):
    x = int(input("enter the next value: "))
    vals.append(x)
print(vals)
# for i in vals:
#     print(i)

# searching program

ele = int(input("enter the number for search: "))
for i in range(len(vals)):
    if vals[i] == ele:
        print(i)
        break

# inbuilt method to find index

print(vals.index(2))