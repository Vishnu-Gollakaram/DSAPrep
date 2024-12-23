from collections import deque

class Solution:
    def findCircleNum(self, adj):
        V = len(adj)  # Number of nodes (cities)
        vis = [False] * V  # Visited array
        connected_comp = 0  # Count of connected components (provinces)
        q = deque()  # Queue for BFS
                
        for node in range(V):
            if not vis[node]:
                connected_comp += 1  # New connected component found
                q.append(node)
                vis[node] = True

                while q:
                    cur = q.popleft()  # Current node
                    for neighbour in range(V):
                        if adj[cur][neighbour] == 1 and not vis[neighbour]:
                            q.append(neighbour)
                            vis[neighbour] = True
                
        return connected_comp
