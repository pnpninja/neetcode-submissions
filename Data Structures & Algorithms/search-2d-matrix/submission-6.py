class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, btm = 0, ROWS - 1
        while top <= btm:
            row = (top + btm) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                btm = row - 1
            else:
                break
    
        if not (top <= btm):
            return False
        row = (top + btm) // 2
        left, right = 0, COLS - 1
        while left <= right:
            if left == right:
                if matrix[row][left] == target:
                    return True
                return False
            elif left + 1 == right:
                if matrix[row][left] == target or matrix[row][right] == target:
                    return True
                else:
                    return False
            else:
                mid = (left + right) // 2
                if target == matrix[row][mid]:
                    return True
                elif target > matrix[row][mid]:
                    left = mid
                else:
                    right = mid
        return False
