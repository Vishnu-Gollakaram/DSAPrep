class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Take 
        # Leave fully
        n = len(coins)
        mem = {}
        def minCoins(n, amount):
            if amount == 0:
                return 0
            if n == 0:
                return float('inf')
            if mem.get((n, amount)):
                return mem[(n, amount)]
            if amount < coins[n - 1]:
                mem[(n, amount)] = minCoins(n - 1, amount)
            else:
                mem[(n, amount)] = min(minCoins(n - 1, amount), 1 + minCoins(n, amount - coins[n - 1]))
            return mem[(n, amount)]
        ans = minCoins(n, amount)
        if ans == float('inf'):
            return -1
        return ans