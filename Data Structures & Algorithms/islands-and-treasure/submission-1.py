class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        INF = 2147483647
        queue = deque()
        visited = set()
        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == 0:
                    queue.append((row, col, 0))
                    visited.add((row, col))
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        while queue:

            row, col, dist = queue.popleft()
            grid[row][col] = dist
            for dr, dc in directions:

                nr, nc = row + dr, col + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1 and (nr, nc) not in visited:

                    new_dist = dist + 1
                    visited.add((nr, nc))
                    queue.append((nr, nc, new_dist))




