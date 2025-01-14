from typing import List
from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Create adjacency list
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))  # Undirected graph

        def dijkstra(src):
            distances = [float('inf')] * n
            distances[src] = 0
            min_heap = [(0, src)]  # (distance, node)

            while min_heap:
                dist, node = heappop(min_heap)
                if dist > distances[node]:
                    continue
                for neighbor, weight in adj[node]:
                    if distances[neighbor] > dist + weight:
                        distances[neighbor] = dist + weight
                        heappush(min_heap, (distances[neighbor], neighbor))
            return distances

        # Find the number of reachable cities for each city
        min_count = float('inf')
        result_city = -1

        for city in range(n):
            distances = dijkstra(city)
            count = sum(1 for d in distances if d <= distanceThreshold)
            
            # Update result: prioritize larger city index in case of ties
            if count < min_count or (count == min_count and city > result_city):
                min_count = count
                result_city = city

        return result_city
