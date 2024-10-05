'''
This is my intuition based 1-D DP
T: O(n*n)
S: O(n)
class Solution:
    # minTillHere = inf
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [float('inf')] * length
        dp[0] = 0
        
        #condition : minTillHere = min(pre_jump + 1, minTillHere)
        for idx in range(length - 1):
            v = nums[idx]
            for ch_idx in range(idx + 1, idx + v + 1):
                if ch_idx == length:
                    break
                dp[ch_idx] = min(dp[idx] + 1, dp[ch_idx])
                
        return dp[length - 1]
'''

# track maximum reached in each greedy jump and
# update maximum greedy reached with max reachable 
# add +1 as we made a jump

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        max_reached = 0
        max_greedy_index = 0
        for i in range(len(nums) - 1):
            max_reached = max(max_reached, i + nums[i])
            if i == max_greedy_index:
                jumps += 1
                max_greedy_index = max_reached
        return jumps
    
