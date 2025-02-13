from heapq import heappush, heappop

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        h = []
        extra = []
        ans = 0

        for n in nums:
            if n < k:
                heappush(h, n)
            else:
                extra.append(n)

        while h:
            x = heappop(h)
            if len(h) == 0:
                y = min(extra)
            else:
                y = heappop(h)
            res = x * 2 + y
            if k > res:
                heappush(h, res)
            else:
                extra.append(res)
            ans += 1

        return ans