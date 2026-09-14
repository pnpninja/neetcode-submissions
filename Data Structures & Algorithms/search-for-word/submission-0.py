DIRS = [[0,1],[0,-1],[1,0],[-1,0]]
class Solution:
    def __init__(self):
        self.rows = 0
        self.cols = 0
    def isValid(self, row: int, col: int):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False
        return True

    def recur(self, board: List[List[str]], row: int, col: int, word: str, ind: int) -> bool:
        if ind == len(word):
            return True
        if not self.isValid(row, col):
            return False
        if word[ind] != board[row][col]:
            return False
        temp = board[row][col]
        board[row][col] = '-'
        found = False
        for dir in DIRS:
            if self.recur(board, row + dir[0], col + dir[1], word, ind + 1):
                found = True
                break
        board[row][col] = temp
        return found

        
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                if self.recur(board, row, col, word, 0):
                    return True
        return False