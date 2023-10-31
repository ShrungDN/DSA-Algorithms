# returns i where all arr[:i] is less than x
# r initilizaed to len(arr) and not len(arr)-1 -> so that if all elements are smaller, the result is still consistent
def bisect_left(arr, x):
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] < x:
            l = m + 1
        else:
            r = m
    return l

arr = [1, 3, 5, 7]

print(bisect_left(arr, 0))
print(bisect_left(arr, 2))
print(bisect_left(arr, 4))
print(bisect_left(arr, 5))
print(bisect_left(arr, 6))
print(bisect_left(arr, 8))