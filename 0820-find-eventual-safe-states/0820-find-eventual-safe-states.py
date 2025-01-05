class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(node):
            visited[node]=1
            path_visited[node]=1
            for i in graph[node]:
                if(visited[i]==0):
                    if(dfs(i)==True):
                        check[i]=0
                        return True
                elif(path_visited[i]):#cycle present in same path
                    check[i]=0
                    return True            
            path_visited[node]=0
            check[node]=1
            return False
        
        n=len(graph)
        visited=[ 0 for i in range(n)]
        path_visited=[ 0 for i in range(n)]
        check=[0 for i in range(n)]
        for i in range(n):
            if(visited[i]==0):
                dfs(i)
        ans=[]
        for i in range(n):
            if(check[i]==1):
                ans.append(i)
        return ans