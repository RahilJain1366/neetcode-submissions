class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])

        def backtrack(row, col):

            if row > rows - 1 or col > cols - 1 or row < 0 or col < 0 or grid[row][col] == 0:
                return 0

            grid[row][col] = 0

            return 1 + (backtrack(row + 1, col) +
                        backtrack(row - 1, col) +
                        backtrack(row, col + 1) +
                        backtrack(row, col - 1))

          
        max_area = 0
        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == 1:
                    area = backtrack(row, col)
                    max_area = max(area, max_area)

        return max_area     
