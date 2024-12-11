#User function Template for python3
from collections import deque

class Solution:
    #Function to find maximum of each subarray of size k.
    def maxOfSubarrays(self, arr, k):
        # code here
        ans = []
        bucket = deque()
        n = len(arr)
        
        for right in range(n):
            while bucket and arr[bucket[-1]] < arr[right]:
                bucket.pop()
                
            bucket.append(right)
            
            if right >= k - 1:
                
                if bucket[0] < right - k + 1:
                    bucket.popleft()
                    
                ans.append(arr[bucket[0]])
                
        return ans