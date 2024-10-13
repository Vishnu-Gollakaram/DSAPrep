class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def gen_braces(n, pattern, op, cl, max_op):
            if n == 0:
                ans.append(pattern)
                return
            
            if op < max_op:
                gen_braces(n - 1, pattern + "(", op + 1, cl, max_op)

            if cl < op:
                gen_braces(n - 1, pattern + ")", op, cl + 1, max_op)

        gen_braces(n * 2, "", 0, 0, n)
        return ans