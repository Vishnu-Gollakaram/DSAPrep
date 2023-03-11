def selectionSort(arr):
    for i in range(len(arr)-1):
        maxPos = i
        for j in range(i+1,len(arr)):
            if arr[j] > arr[maxPos]:
                maxPos = j
        arr[i], arr[maxPos] = arr[maxPos], arr[i]
    return arr