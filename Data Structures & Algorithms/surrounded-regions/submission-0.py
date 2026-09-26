class Solution:
    def solve(self, board: List[List[str]]) -> None:

        if not board and not board[0]:
            return None

        rows, cols = len(board), len(board[0])


        def backtrack(row, col):

            if row < 0 or col < 0 or row > rows - 1 or col > cols - 1 or board[row][col] != 'O':
                return 
            
            board[row][col] = 'T'

            backtrack(row + 1, col)
            backtrack(row - 1, col)
            backtrack(row, col + 1)
            backtrack(row, col - 1)

        
        for row in range(rows):
            backtrack(row, 0)
            backtrack(row, cols - 1)

        for col in range(cols):

            backtrack(0, col)
            backtrack(rows - 1, col)

        for row in range(rows):
            for col in range(cols):

                if board[row][col] == 'O':
                    board[row][col] = 'X'
                
                elif board[row][col] == 'T':
                    board[row][col] = 'O'
        