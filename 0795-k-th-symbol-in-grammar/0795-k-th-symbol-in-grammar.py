class Solution:
    '''
    0
    0 | 1
    01 | 10
    0110 | 1001

    As one can observe, row n + 1 is copy of row n in first half and compelent of row n in  second half. 

    Hence, the idea is we can reduce: n, k such that it goes down to n = 1, k = 1 (base case)

    If k comes after mid we would return 1's compelemt of value or we would return k
    '''
    def kthGrammar(self, n: int, k: int) -> int:

        def k_helper(n, k):
            mid = 2 **(n - 2)
   
            if n == 1 and k == 1:
                return 0
            
            if k <= mid:
                return k_helper(n - 1, k)

            return 1 - k_helper(n - 1, k - mid)

        return k_helper(n, k)