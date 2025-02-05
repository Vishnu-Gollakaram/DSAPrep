class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            '2':['a', 'b', 'c'],
            '3':['d', 'e', 'f'],
            '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z']
        }
        ans = []
        n = len(digits)

        def updt(n, s):
            print(n)
            if n == 0:
                ans.append(s)
                return
            digit = digits[n - 1]
            vals = d[digit]

            for k in range(len(vals)):
                updt(n - 1, vals[k] + s)

        if n > 0:updt(n, '')
        return ans