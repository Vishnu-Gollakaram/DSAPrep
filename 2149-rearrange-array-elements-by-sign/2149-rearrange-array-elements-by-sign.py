from collections import deque

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posDeque = deque()
        negDeque = deque()
        ans = []
        
        for i in nums:
            if i < 0:
                if not ans or ans[-1] < 0:
                    negDeque.append(i)
                else:
                    if not negDeque:
                        ans.append(i)
                    else:
                        ans.append(negDeque.popleft())
                        negDeque.append(i)
            else:
                if not ans or ans[-1] < 0:
                    if not posDeque:
                        ans.append(i)
                    else:
                        ans.append(posDeque.popleft())
                        posDeque.append(i)
                else:
                    posDeque.append(i)
        
        if not nums:
            return []
        
        if not ans or ans[-1] < 0:
            for _ in range(len(negDeque)):
                ans.append(posDeque.popleft())
                ans.append(negDeque.popleft())
        else:
            for _ in range(min(len(negDeque), len(posDeque))):
                ans.append(negDeque.popleft())
                ans.append(posDeque.popleft())
            ans.append(negDeque.popleft())
        
        return ans
