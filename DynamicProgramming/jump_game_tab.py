class Solution:
    def jump(self, nums):
        length = len(nums)
        mem = [-1] * length
        
        def jump_help(cur):
            mem[-1] = 0

            for i in range(length - 2, -1, -1):
                j = i + nums[i]
                mem[i] = 1 + mem[i + 1]

                for k in range(i + 2, min(j + 1, length)):
                    mem[i] = min(mem[i], 1 + mem[k])

            return mem[cur]

        op = jump_help(0)
        return op