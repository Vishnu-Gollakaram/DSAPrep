class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        dic = {}
        ans = []

        for word in words2:
            cc = {}
            for key in word:
                cc[key] = cc.get(key, 0) + 1
            for key in cc:
                dic[key] = max(dic.get(key, 0), cc[key])

        for word in words1:
            d = {}
            for key in word:
                d[key] = d.get(key, 0) + 1
            for key in dic:
                if d.get(key, 0) < dic[key]:
                    break
            else:
                ans.append(word)

        return ans