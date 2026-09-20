class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1

        queue = deque()

        for node in range(len(indegree)):
            if indegree[node] == 0:
                queue.append(node)
        count = 0
        while queue:

            for _ in range(len(queue)):

                node = queue.popleft()
                count += 1

                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)

        return count == numCourses

