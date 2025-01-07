class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        n = len(words)
        for i in range(n):
            word = words[i]
            for j in words[:i] + words[i+1:]:
                print(word, j)
                if word in j:
                    ans.append(word)
                    break
        return ans