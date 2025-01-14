# User function Template for python3
from typing import List
from heapq import heappush, heappop

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 1_000_000_007  # Modulo for the result

        # Initialize distances and ways
        distances = [float('inf')] * n
        ways = [0] * n

        # Build the adjacency list
        adj = [[] for _ in range(n)]
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # Priority queue for Dijkstra's Algorithm
        distances[0] = 0
        ways[0] = 1
        pq = [(0, 0)]  # (current_distance, current_node)

        while pq:
            w, node = heappop(pq)

            # If we've already processed a shorter distance, skip
            if w > distances[node]:
                continue

            # Process neighbors
            for neigh, weight in adj[node]:
                nw = w + weight

                if distances[neigh] > nw:
                    # Found a shorter path
                    distances[neigh] = nw
                    ways[neigh] = ways[node]
                    heappush(pq, (nw, neigh))
                elif distances[neigh] == nw:
                    # Found an alternative shortest path
                    ways[neigh] = (ways[neigh] + ways[node]) % MOD

        return ways[n - 1]
