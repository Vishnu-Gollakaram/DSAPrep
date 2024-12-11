class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * len(code)
        elif k < 0:
            i = 0
            ans = []
            while i < n:
                if i == 0:
                    ans.append(sum(code[k:]))
                elif i + k < 0:
                    ans.append(sum(code[i + k :]) + sum(code[:i]))
                else:
                    ans.append(sum(code[i + k : i]))
                i += 1
            return ans
        else:
            i = n - 1
            ans = []
            while i > -1:
                if i == 0:
                    ans.append(sum(code[1 : k + 1]))
                elif i + k < n:
                    ans.append(sum(code[i + 1 : i + k + 1]))
                else:
                    ans.append(sum(code[i + 1 : i + k + 2]) + sum(code[: i + k - n + 1]))
                i -= 1
            return ans[::-1]