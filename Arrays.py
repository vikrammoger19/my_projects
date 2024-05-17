from array import *

vals = array('i', [1, 2, 3, 4, 5])
print(vals)
vals.insert(3, 8)
print(vals)
vals.remove(2)
print(vals)
vals.reverse()
print(vals)
print(vals.buffer_info())

for i in vals:
    print(i)

# for creating character array

arr = array('u', ['p', 'y', 't', 'h', 'o', 'n'])
for i in arr:
    print(i)

newArr = array(vals.typecode, (a ** 3 for a in vals))
for i in newArr:
    print(i)
