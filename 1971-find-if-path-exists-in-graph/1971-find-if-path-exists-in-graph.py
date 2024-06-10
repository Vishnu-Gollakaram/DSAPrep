class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, dest: int) -> bool:
        if edges == [] or source == dest:
            return True
        def create_adj_list(edges, n):
            adj_list = [[] for _ in range(n)]
            for edge in edges:
                u, v = edge[0], edge[1]
                adj_list[u].append(v)
                adj_list[v].append(u)
            return adj_list
        
        adj_list = create_adj_list(edges, n)
        
        vis = set()
        def bfs(source, dest, n):
            vis.add(source)
            q = [source]
            while q:
                node = q.pop(0)
                for neighbour in adj_list[node]:
                    if neighbour not in vis:
                        vis.add(neighbour)
                        q.append(neighbour)
                        if neighbour == dest:
                            return True
            return False
        
        return bfs(source, dest, n)