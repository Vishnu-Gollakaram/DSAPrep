class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        ans = []
        n = len(nums)
        if n == 0: return ans
        range_start = f"{nums[0]}"

        for i in range(1, n):
            if nums[i] != 1 + nums[i - 1]:
                if str(nums[i - 1]) != range_start:
                    range_start += f"->{nums[i - 1]}"
                ans.append(range_start)
                range_start = f"{nums[i]}"

        if str(nums[-1]) != range_start:
            range_start += f"->{nums[-1]}"
        ans.append(range_start)
        
        return ans