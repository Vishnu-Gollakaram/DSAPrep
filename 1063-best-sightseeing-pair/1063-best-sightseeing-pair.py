class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_i = values[0]
        n = len(values)
        ans = 0

        for ind in range(1, n):
            ans = max(ans, max_i + values[ind] - ind)
            max_i = max(max_i, values[ind] + ind)

        return ans      