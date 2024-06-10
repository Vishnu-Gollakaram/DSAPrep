from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, dest: int) -> bool:
        if source == dest:
            return True
        
        def create_adj_list(edges, n):
            adj_list = [[] for _ in range(n)]
            for u, v in edges:
                adj_list[u].append(v)
                adj_list[v].append(u)
            return adj_list
        
        adj_list = create_adj_list(edges, n)
        
        visited = set()
        
        def bfs(source, dest):
            queue = deque([source])
            visited.add(source)
            
            while queue:
                node = queue.popleft()
                for neighbor in adj_list[node]:
                    if neighbor == dest:
                        return True
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            return False
        
        return bfs(source, dest)
