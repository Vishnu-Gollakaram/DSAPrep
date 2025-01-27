from collections import deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[b].append(a)
        
        pre_req = [set() for i in range(numCourses)]
        for node in range(numCourses):
            q = deque()
            q.append(node)
            while q:
                cur = q.popleft()
                for neigh in adj[cur]:
                    if neigh not in pre_req[node]:
                        q.append(neigh)
                        pre_req[node].add(neigh)
        # print(pre_req)
        ans = []
        for u, v in queries:
            ans.append( u in pre_req[v])
        return ans