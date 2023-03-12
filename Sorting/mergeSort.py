def mergeSort(arr):
    if len(arr)<=1: return #Split recursively till array has 1 element each
    m = len(arr)//2
    l = arr[:m] #split into left and right parts
    r = arr[m:]
    mergeSort(l) #mergeSort each sub array
    mergeSort(r)
    i, j, k = 0, 0, 0
    while (i<len(l) and j<len(r)):
        if l[i]<r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k+=1
    while i<len(l):
        arr[k] = l[i]
        i+=1
        k += 1
    while j< len(r):
        arr[k] = r[j]
        j += 1
        k += 1
arr = [1,3,6,2,-2]
mergeSort(arr)
print(arr)