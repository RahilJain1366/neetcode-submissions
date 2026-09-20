class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        indegree = [0] * numCourses

        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        
        queue = deque()
        res = []

        for node in range(len(indegree)):
            if indegree[node] == 0:
                queue.append(node)

        while queue:

            for _ in range(len(queue)):

                node = queue.popleft()
                res.append(node)

                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)

        return res if len(res) == numCourses else []
