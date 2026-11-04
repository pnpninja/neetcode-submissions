class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        rowIter, colIter = 0, cols - 1

        while rowIter < rows and colIter >= 0:
            if target == matrix[rowIter][colIter]:
                return True
            elif target > matrix[rowIter][colIter]:
                rowIter+=1
            else:
                colIter-=1
        return False
            