class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(0, 9, 1)]
        cols = [set() for _ in range(0, 9, 1)]
        grid = [set() for _ in range(0, 9, 1)]
        for row in range(0, 9, 1):
            for col in range(0, 9, 1):
                if board[row][col] == ".":
                    continue
                num = int(board[row][col])
                if num in rows[row]:
                    return False
                if num in cols[col]:
                    return False
                gridNum = (int(row / 3) * 3) + int(col / 3)
                if num in grid[gridNum]:
                    return False
                rows[row].add(num)
                cols[col].add(num)
                grid[gridNum].add(num)
        return True

