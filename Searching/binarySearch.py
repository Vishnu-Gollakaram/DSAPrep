def binarySearch(arr,target):
	l = 0
    h = len(arr)-1
    #if mid element euqls target then return mid index
    #if middle element greater than target, then shift upper limit to mid - 1
    #if middle element less than target, then shift lower limit to mid + 1
    while l<=h:
        mid = (l+h)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]>target:
            h = mid - 1
        else:
            l = mid + 1
    return -1