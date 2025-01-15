from collections import deque

class Solution:

    def minimizeXor(self, num1: int, num2: int) -> int:

        ct_1 = bin(num2).count('1')

        b_num1 = bin(num1)[2:]

        ans = deque([0] * len(b_num1))
        print(b_num1, ct_1)

        for i in range(len(b_num1)):

            if ct_1 == 0:

                break

            if b_num1[i] == '1':

                ans[i] += 1
                ct_1 -= 1
                
            #print(ans, ct_1, i)

        ptr = len(b_num1)
        print(ans)

        while ct_1:


            if ptr < 1:

                ans.appendleft(1)

                ct_1 -= 1

            elif ans[ptr - 1] == 0:

                ans[ptr - 1] = 1

                ct_1 -= 1

            ptr -= 1
            
        print(ans)

            

        return int(''.join([str(i) for i in ans]), 2)