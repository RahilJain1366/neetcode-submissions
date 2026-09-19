class UnionFind:

    def __init__(self, n):

        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):

        rootX, rootY = self.find(x), self.find(y)

        if rootX == rootY:
            return False

        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY

        elif self.rank[rootY] < self.rank[rootX]:
            self.parent[rootY] = rootX

        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

        return True


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])
        uf = UnionFind(m * n)
        visited = set()
        num_of_islands = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    num_of_islands += 1

                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc

                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1":
                            curr = row * n + col
                            neigh = nr * n + nc

                            if uf.union(curr, neigh):
                                num_of_islands -= 1

        return num_of_islands



                        




        