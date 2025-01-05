from collections import deque

class Solution:
    def isBipartite(self, adj):
        n = len(adj)
        vis = [-1] * n  # -1: not visited, 0: color A, 1: color B

        def dfs(nod):
            for node in adj[nod]:
                if vis[node] == -1:  # Not visited
                    vis[node] = 1 - vis[nod]  # Assign opposite color
                    if not dfs(node):
                        return False
                elif vis[node] == vis[nod]:  # Conflict in coloring
                    return False
            return True

        for node in range(n):
            if vis[node] == -1:  # Unvisited node
                vis[node] = 0  # Assign initial color
                if not dfs(node):
                    return False

        return True
