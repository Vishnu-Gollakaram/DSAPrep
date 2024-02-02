powTen = 2
ans = []
for powTen in range(2, 10):
    dig = "0"
    for i in range(1, powTen):
        dig += str(i)
    for s in range(powTen, 10):
        dig = dig[1:] + str(s)
        ans.append(int(dig))
# print(ans)

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ret = []
        for i in ans:
            if i > high:
                break
            elif i < low:
                continue
            else:
                ret.append(i)
        return ret
            