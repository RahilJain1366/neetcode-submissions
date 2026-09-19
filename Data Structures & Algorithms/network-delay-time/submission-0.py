import collections

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        edges = collections.defaultdict(list)

        for u,v,w in times:
            edges[u].append([v,w])

        minHeap = [(0,k)]
        t = 0
        visited = set()

        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            
            t = max(t, cost)

            for new_node, new_cost in edges[node]:
                if new_node not in visited:
                    heapq.heappush(minHeap, (cost + new_cost, new_node))

        return t if n == len(visited) else -1


