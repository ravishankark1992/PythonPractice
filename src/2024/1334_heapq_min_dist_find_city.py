# https://www.youtube.com/watch?v=--wKPR3ByJc
import heapq
from typing import List, Tuple
from collections import defaultdict
from math import inf

# The following code implements Dijkstra's algorithm to find the city with the minimum number of cities that are reachable within the given distance threshold.
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        visited=[]
        cost = {}
        adj = defaultdict(list)
        for v0, v1, w in edges:
            adj[v0].append((v1, w))
            adj[v1].append((v0, w))
        print(adj)
        
        def dijksha(root):
            visited = set()
            
            heap = [(0, root)]
            total_dist = 0
            while heap:
                dist, node = heapq.heappop(heap)
                if node in visited:
                    continue
                visited.add(node)
                for nei, next_dist in adj[node]:
                    
                    nei_dist = next_dist+dist
                    if nei_dist<=distanceThreshold:
                        heapq.heappush(heap, (nei_dist, nei))
            
            return len(visited)-1

        min_count=float(inf)
        for node in range(n):
            count = dijksha(node)
            if count<=min_count:
                min_count = count
                result = node
        return result