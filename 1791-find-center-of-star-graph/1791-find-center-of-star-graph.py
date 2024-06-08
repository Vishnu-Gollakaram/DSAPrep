class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = 0
        for edge in edges:
            n = max(edge[0], edge[1], n)
        reachable = [0] * (n + 1)
        for edge in edges:
            reachable[edge[0]] += 1
            reachable[edge[1]] += 1
        for ind in range(n + 1):
            if reachable[ind] == n - 1:
                return ind