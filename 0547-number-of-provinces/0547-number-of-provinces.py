class Solution:
    def findCircleNum(self, adj):
        V = len(adj)
        vis = [False] * (V)
        conected_comp = 0
                
        def dfs_rec(node):
            vis[node - 1] = True
            
            for neighbour in range(V):
                if adj[node - 1][neighbour] == 1 and not vis[neighbour]:
                    dfs_rec(neighbour + 1)
                
        for node in range(1, V + 1):
            if vis[node - 1] == False:
                conected_comp += 1
                dfs_rec(node)
                
        return conected_comp