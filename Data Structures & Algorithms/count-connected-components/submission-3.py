class UnionFind:

    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.count = n
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

        self.count -= 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        uf = UnionFind(n)
        count = 0
        for u, v in edges:
            uf.union(u,v)

        return uf.count









        