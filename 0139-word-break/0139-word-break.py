class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)  # Using a set for fast lookups
        n = len(s)
        
        # dp[i] will be True if s[0:i] can be segmented into words in wordDict
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty string can always be segmented
        
        # Precompute the maximum word length to optimize loop boundaries
        max_word_len = max(len(word) for word in word_set)
        
        # Start building the dp array
        for i in range(1, n + 1):
            for j in range(max(0, i - max_word_len), i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # No need to check further, found a valid segmentation

        return dp[n]
