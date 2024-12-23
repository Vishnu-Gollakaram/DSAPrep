from collections import deque
class Solution:
    def findCircleNum(self, adj):
        V = len(adj)
        vis = [False] * (V)
        conected_comp = 0
        q = deque()
                
        for node in range(V):
            if vis[node] == False:
                conected_comp += 1
                q.append(node)
                vis[node] = True

            while q:
                cur = q.popleft()
                for neighbour in range(V):
                    if adj[cur][neighbour] == 1 and not vis[neighbour]:
                        q.append(neighbour)
                        vis[neighbour] = True
                
        return conected_comp