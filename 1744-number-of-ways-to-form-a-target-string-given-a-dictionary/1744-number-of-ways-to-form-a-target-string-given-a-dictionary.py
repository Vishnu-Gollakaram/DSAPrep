class Solution:
    def numWays(self, words: List[str], tar: str) -> int:
        MOD = 10**9 + 7
        n = len(words)
        p = len(words[0])
        t = len(tar)

        # Step 1: Preprocess character frequencies in each column
        char_count = [[0] * p for _ in range(26)]  # 26 letters in the alphabet
        for word in words:
            for k, ch in enumerate(word):
                char_count[ord(ch) - ord('a')][k] += 1

        # Step 2: Initialize two 1D arrays for current and next state
        curr = [0] * (p + 1)  # Current row (dp[i])
        next = [1] * (p + 1)  # Next row (dp[i + 1]), base case where dp[t][k] = 1 for all k

        # Step 3: Fill the dp arrays bottom-up
        for i in range(t - 1, -1, -1):  # Iterate over target string in reverse
            curr = [0] * (p + 1)  # Reset the current row
            for k in range(p - 1, -1, -1):  # Iterate over columns in reverse
                # Calculate dp[i][k] based on dp[i + 1][k + 1] (next[k + 1]) and dp[i][k + 1] (curr[k + 1])
                curr[k] = (char_count[ord(tar[i]) - ord('a')][k] * next[k + 1]) % MOD
                curr[k] = (curr[k] + curr[k + 1]) % MOD

            # Swap current and next for the next iteration
            next = curr

        # Step 4: The answer is stored in curr[0], representing dp[0][0]
        return curr[0]
