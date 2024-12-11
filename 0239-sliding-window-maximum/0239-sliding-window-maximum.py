class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
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