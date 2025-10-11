class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        if not power:
            return 0

        earn = {}

        for i in power:
            if earn.get(i):
                earn[i] += i
            else:
                earn[i] = i

        vals = list(earn.keys())
        vals.sort()
        n = len(vals)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            nxt = bisect_left(vals, vals[i] + 3)
            take = earn[vals[i]] + dp[nxt]
            skip = dp[i + 1]
            dp[i] = max(take, skip)

        return dp[0]