class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        if not power:
            return 0

        power.sort()
        vals, earn = [], []

        i = 0
        while i < len(power):
            v = power[i]
            tot = 0
            while i < len(power) and power[i] == v:
                tot += v
                i += 1

            vals.append(v)
            earn.append(tot)

        n = len(vals)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            nxt = bisect_left(vals, vals[i] + 3)
            take = earn[i] + dp[nxt]
            skip = dp[i + 1]
            dp[i] = max(take, skip)

        return dp[0]