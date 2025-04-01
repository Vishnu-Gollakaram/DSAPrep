from typing import List

class Solution:
    def findMin(self, arr: List[int]) -> int:
        start = 0
        end = len(arr) - 1
        
        while start < end:
            mid = (start + end) // 2
            
            if arr[mid] > arr[end]:  
                # Min must be in the right half
                start = mid + 1
            elif arr[mid] < arr[end]:  
                # Min must be in the left half or at mid
                end = mid
            else:  
                # When arr[mid] == arr[end], we can't determine the side, so reduce `end`
                end -= 1
        
        return arr[start]  # Start will point to the minimum element
