class Solution:
    def calculateBox(self, row: int, col: int) -> int:
        return ((row // 3) * 3) + (col // 3)
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSeen, colSeen, boxSeen = defaultdict(set), defaultdict(set), defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    if board[row][col] in rowSeen[row]:
                        return False
                    if board[row][col] in colSeen[col]:
                        return False
                    box = self.calculateBox(row, col)
                    if board[row][col] in boxSeen[box]:
                        return False
                    rowSeen[row].add(board[row][col])
                    colSeen[col].add(board[row][col])
                    boxSeen[box].add(board[row][col])
        return True