class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(s, target, index=0, curr_sum=0):
            """Check if square string `s` can be partitioned to sum to `target`."""
            if index == len(s):
                return curr_sum == target
            
            num = 0
            for j in range(index, len(s)):
                num = num * 10 + int(s[j])  # Form number from substring
                if curr_sum + num <= target and can_partition(s, target, j + 1, curr_sum + num):
                    return True
            return False

        punishment_sum = 0
        for i in range(1, n + 1):
            squared = str(i * i)
            if can_partition(squared, i):
                punishment_sum += i * i
        
        return punishment_sum