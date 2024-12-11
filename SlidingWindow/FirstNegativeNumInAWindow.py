from collections import deque

class Solution:
    def FirstNegativeInteger(self, arr, k):
        n = len(arr)
        right = 0
        left = 0
        ans = []
        bucket = deque()
        
        while right < n:
            
            if arr[right] < 0:
                bucket.append(arr[right])
                
            if right - left + 1 == k:
                
                if len(bucket) == 0:
                    ans.append(0)
                else:
                    ans.append(bucket[0])
                
                if arr[left] < 0:
                    bucket.popleft()
                    
                left += 1
                right += 1
                
            else:
                right += 1
                
        return ans