class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])

        atlantic = set()
        pacific = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def backtrack(row, col, ocean):

            ocean.add((row,col))

            for dr, dc in directions:

                nr, nc = row + dr, col + dc

                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in ocean and heights[nr][nc] >= heights[row][col]:

                    backtrack(nr, nc, ocean)

        for row in range(rows):
            backtrack(row, 0, pacific)

        for col in range(cols):
            backtrack(0, col, pacific)

        for row in range(rows):
            backtrack(row, cols - 1, atlantic)
        
        for col in range(cols):
            backtrack(rows - 1, col, atlantic)

        res = []
        for row in range(rows):
            for col in range(cols):

                if (row, col) in atlantic and (row, col) in pacific:
                    res.append([row,col])

        return res