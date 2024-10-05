class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            if not d.get(i):
                d[i] = 1
            else:
                d[i] += 1
        keyVals = []
        for k in d.keys():
            keyVals.append([k, d[k]])
        keyVals.sort(key = lambda x:(x[1], x[0]))
        ans = ""
        for i in keyVals:
            ans += (i[0] * i[1])
        return ans[::-1]