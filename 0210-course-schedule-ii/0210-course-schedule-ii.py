class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        
        for it in prerequisites:
            adj[it[1]].append(it[0])
            in_degree[it[0]] += 1
        
        q = deque()
        ans = []
                
        for node in range(n):
            if in_degree[node] == 0:
                q.append(node)
                
        while q:
            node = q.popleft()
            ans.append(node)
            
            for neigh in adj[node]:
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    q.append(neigh)
                    
        if len(ans) != n:
            return []
            
        return ans