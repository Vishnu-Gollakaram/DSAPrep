class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        su = sum(nums)

        if su & 1:
            return False
        su //= 2
        
        mem = [False] * (su + 1)

        def sub_sum(n, su):
            mem[0] = True

            for i in range(1, n + 1):
                for j in range(su, nums[i - 1] - 1, -1):
                    mem[j] = mem[j] or mem[j - nums[i - 1]]

            return mem[su]

        return sub_sum(len(nums), su)