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

        # Step 2: DP Table Initialization
        dp = [[0] * (p + 1) for _ in range(t + 1)]

        # Base Case: If the entire target is formed, there's 1 way (i.e., an empty target)
        for k in range(p + 1):
            dp[t][k] = 1

        # Step 3: Fill the DP table
        for i in range(t - 1, -1, -1):  # Iterate over target string in reverse
            for k in range(p - 1, -1, -1):  # Iterate over columns in reverse
                # If the target character tar[i] matches some characters in column k
                dp[i][k] = (char_count[ord(tar[i]) - ord('a')][k] * dp[i + 1][k + 1]) % MOD
                # Add the case where we skip column k
                dp[i][k] = (dp[i][k] + dp[i][k + 1]) % MOD

        # Step 4: The answer is dp[0][0], the number of ways to form the entire target from column 0
        return dp[0][0]
