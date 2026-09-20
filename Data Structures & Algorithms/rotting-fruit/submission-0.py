class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        fresh_oranges = 0
        rotten = deque()

        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == 1:
                    fresh_oranges += 1
                elif grid[row][col] == 2:
                    rotten.append((row, col))

        if fresh_oranges == 0:
            return 0

        directions = [(1,0),(0,1),(0,-1),(-1,0)]
        minutes = -1

        while rotten:

            for _ in range(len(rotten)):
                row, col = rotten.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        rotten.append((nr, nc))
                        fresh_oranges -= 1

            minutes += 1

        return minutes if fresh_oranges == 0 else -1




