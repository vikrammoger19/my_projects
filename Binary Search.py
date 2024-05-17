def binarySearch(arr, first, last, key):
    mid = (first + last) // 2
    while first < last:
        if arr[mid] < key:
            first = mid + 1
        elif arr[mid] == key:
            return mid
        else:
            last = mid - 1

        mid = (first + last) // 2
    return -1


my_list = [1, 2, 3, 4, 5]
x = 8
high = len(my_list) - 1
result = binarySearch(my_list, 0, high, x)

if result != -1:
    print("element found at index: ", result)
else:
    print("element not found:")
