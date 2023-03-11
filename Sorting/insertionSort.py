def insertionSort(arr):
    for i in range(1,len(arr)):
        j = i-1
        key = arr[i]
        while j>-1 and key<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    print(arr)
insertionSort([1,3,6,2,-2])