class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def backtrack(row, col, index):
            
            if index == len(word):
                return True
            
            if row < 0 or row >= rows or col < 0 or col >= cols :
                return False
            
            if board[row][col] != word[index]:
                return False
            
            board[row][col] = "#"

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if backtrack(nr, nc, index + 1):
                    return True

            board[row][col] = word[index]

        for row in range(rows):
            for col in range(cols):

                if backtrack(row, col, 0):
                    return True

        return False