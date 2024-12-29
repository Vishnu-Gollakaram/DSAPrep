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

        # Memoization dictionary
        vis = {}

        # Step 2: Recursive function to count ways
        def get_tar_ways(i, k):
            if i == t:  # Successfully matched all characters in target
                return 1
            if k == p:  # Reached the end of columns but target is not fully matched
                return 0
            if (i, k) in vis:
                return vis[(i, k)]

            # Step 3: Calculate ways using preprocessed frequencies
            loop_adder = (char_count[ord(tar[i]) - ord('a')][k] * get_tar_ways(i + 1, k + 1)) % MOD
            loop_adder += get_tar_ways(i, k + 1)
            loop_adder %= MOD  # Take modulo to avoid overflow

            vis[(i, k)] = loop_adder
            return loop_adder

        # Step 4: Start the recursion
        return get_tar_ways(0, 0)
