from collections import Counter
from heapq import heappush, heappop

from collections import Counter

def topKFrequent(nums, k):
    # Step 1: Count the frequency of each element
    freq_map = Counter(nums)

    # Step 2: Create buckets based on frequency
    n = len(nums)
    buckets = [[] for _ in range(n + 1)]
    
    for num, freq in freq_map.items():
        buckets[freq].append(num)

    # Step 3: Gather the top K frequent elements
    result = []
    for i in range(n, 0, -1):  # Start from highest frequency
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result  # Stop when we have k elements

    return result


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return topKFrequent(nums, k)
        '''c = Counter(nums)
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
        
        return [i[1] for i in ans]'''