class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        fst_lst = {}
        for i in range(len(s)):
            chr = s[i]
            if chr not in fst_lst:
                fst_lst[chr] = [i]
            else:
                if len(fst_lst[chr]) == 1:
                    fst_lst[chr].append(i)
                else:
                    fst_lst[chr][1] = i
        
        for key in fst_lst.keys():
            if len(fst_lst[key]) == 2:
                ans += len(set(s[fst_lst[key][0] + 1 : fst_lst[key][1]]))

        return ans