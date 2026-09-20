class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        def backtrack(row, col):

            if row > rows - 1 or col > cols - 1 or row < 0 or col < 0 or grid[row][col] == "0":
                return 

            grid[row][col] = "0"

            backtrack(row + 1, col)
            backtrack(row - 1, col)
            backtrack(row, col + 1)
            backtrack(row, col - 1)

        count = 0
        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == "1":
                    backtrack(row, col)
                    count += 1
        
        return count
