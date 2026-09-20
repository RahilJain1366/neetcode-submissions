class UnionFind:

    def __init__(self, n):

        self.parent = [i for i in range(n)]
    
    def find(self, x):

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]
    
    def union(self, x, y):

        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False

        self.parent[rootY] = rootX

        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        uf = UnionFind(n)

        for u, v in edges:

            if not uf.union(u,v):
                return False
        
        return True

