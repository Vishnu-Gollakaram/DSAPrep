class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        def dfs(base):
            if base > n:
                return
            if base > 0:
                ans.append(base)
            start = 0
            if base == 0:
                start = 1

            for unit in range(start, 10):
                lex = (10 * base) + unit

                if (lex) > n:
                    break
                dfs(lex)

        dfs(0)
        return ans