from collections import deque
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        ct_1 = bin(num2).count('1')
        b_num1 = bin(num1)[2:]

        ans = deque([0] * len(b_num1))
        for i in range(len(b_num1)):
            if ct_1 == 0:
                break
            if i == '1':
                ans += 1

        ptr = len(b_num1)
        while ct_1:
            if not ptr:
                ans.appendleft(1)
                ct_1 -= 1
            elif ans[ptr - 1] == 0:
                ans[ptr - 1] = 1
                ct_1 -= 1
            ptr -= 1
            
        return int(''.join([str(i) for i in ans]), 2)