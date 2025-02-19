class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > (3 << (n - 1)):  
            return ""  # If k is too large, return empty string
        
        queue = deque([""])  # Start with an empty string
        
        while k:
            curr = queue.popleft()
            
            for c in "abc":
                if not curr or curr[-1] != c:
                    queue.append(curr + c)
                    if len(curr) + 1 == n:
                        k -= 1
                if k == 0:
                    break
        
        return queue[-1]