from collections import deque

class Solution:
    def hasCycle(self, adjList, src, n):
        q = deque([(src, -1)])
        vis = [False] * (n + 1)
        vis[src] = True

        while q:
            node, parent = q.popleft()
            for x in adjList[node]:
                if not vis[x]:
                    vis[x] = True
                    q.append((x, node))
                elif x != parent:
                    return True
        return False

    def findRedundantConnection(self, edges):
        n = len(edges)
        adjList = [[] for _ in range(n + 1)]

        for src, dest in edges:
            adjList[src].append(dest)
            adjList[dest].append(src)
            if self.hasCycle(adjList, src, n):
                return [src, dest]

        return []
