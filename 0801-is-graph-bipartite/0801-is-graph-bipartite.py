from collections import deque

class Solution:
    def isBipartite(self, adj):
        q = deque()
        n = len(adj)
        vis = [False] * n  # -1: not visited, 0: color A, 1: color B

        for node in range(n):
            if vis[node] == False:  # Unvisited node
                vis[node] = 0  # Assign color A
                q.append((node, 0))
                
                while q:
                    cur, to_set = q.popleft()
                    
                    for neigh in adj[cur]:
                        if vis[neigh] == False:  # Not visited
                            vis[neigh] = 1 - to_set  # Assign opposite color
                            q.append((neigh, 1 - to_set))
                        elif vis[neigh] != (1 - to_set):  # Conflict in coloring
                            return False

        return True