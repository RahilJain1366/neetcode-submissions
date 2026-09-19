class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n, m = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:

            mid = (left + right) // 2
            row, col = divmod(mid, m)

            if matrix[row][col] == target:
                return True

            else:

                if matrix[row][col] < target:
                    left = mid + 1

                else:
                    right = mid - 1

        return False


