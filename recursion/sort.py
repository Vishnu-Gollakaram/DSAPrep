# in-memory approach, modify same data structure (same name)
def sort(arr):
    if len(arr) <= 1:
        return
    last = arr.pop()
    sort(arr)
    insert(arr, last)

def insert(arr, ele):
    if len(arr) == 0 or arr[-1] <= ele:
        arr.append(ele)
        return
    last = arr.pop()
    insert(arr, ele)
    arr.append(last)

arr = [2, 5, 3, 4, 7, 9, 8]
sort(arr)
print(arr)