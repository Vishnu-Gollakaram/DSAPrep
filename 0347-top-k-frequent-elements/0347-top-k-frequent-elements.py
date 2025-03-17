from collections import Counter
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        ans = []
        i = 0

        for key in c:
            if i < k:
                heappush(ans, [c[key], key])
                i += 1
            else:
                if ans[0][0] < c[key]:
                    heappop(ans)
                    heappush(ans, [c[key], key])
        
        return [i[1] for i in ans]
