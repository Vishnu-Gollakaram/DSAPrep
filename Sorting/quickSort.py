def quickSort(arr):
    #if not an empty array, split based on pivot
    #if we have an empty array, return []
    if not arr: return []
    pivot = arr.pop(len(arr)-1)
    l = []
    u = []
    for i in range(len(arr)):
        if arr[i] < pivot:
            l.append(arr[i])
        else:
            u.append(arr[i])
    return quickSort(l)+[pivot]+quickSort(u)
arr = [-5 , -8, 1, 33, 2, 0]
print(quickSort(arr))