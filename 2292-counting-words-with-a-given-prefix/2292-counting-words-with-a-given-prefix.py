class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        p = len(pref)
        for word in words:
            if len(word) >= p:
                if word[:p] == pref:
                    ans += 1

        return ans