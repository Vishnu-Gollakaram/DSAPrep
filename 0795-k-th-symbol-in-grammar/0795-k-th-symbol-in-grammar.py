class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def k_helper(n, k):
            mid = 2 **(n - 2)
   
            if n == 1 and k == 1:
                return 0
            
            if k <= mid:
                return k_helper(n - 1, k)

            return 1 - k_helper(n - 1, k - mid)

        return k_helper(n, k)