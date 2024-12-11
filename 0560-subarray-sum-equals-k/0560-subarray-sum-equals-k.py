class Solution:
    def subarraySum(self, arr: List[int], k: int) -> int:
        prefix_sum_count = {0 : 1}
        n = len(arr)
        prefix_sum = 0
        ans = 0
        
        for i in range(n):
            prefix_sum += arr[i]
            
            if prefix_sum - k in prefix_sum_count:
                ans += prefix_sum_count[prefix_sum - k]
                
            prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1
               
        return ans