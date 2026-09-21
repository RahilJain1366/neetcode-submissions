class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))

        min_heap = [(0,k)]
        visited = set()
        t = 0

        while min_heap:

            cost, node = heapq.heappop(min_heap)

            if node in visited:
                continue

            visited.add(node)

            t = max(t, cost)

            for new_node, new_cost in graph[node]:
                if new_node not in visited:
                    heapq.heappush(min_heap, (cost + new_cost, new_node))
        
        return t if len(visited) == n else -1

        