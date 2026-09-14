class Solution:
    def recur(self, n: int, open: int, close: int, stack: List[str], res: List[str]):
        if open == close == n:
            res.append("".join(stack))
            return
        if open < n:
            stack.append("(")
            self.recur(n, open + 1, close, stack, res)
            stack.pop()
        if close < open:
            stack.append(")")
            self.recur(n, open, close + 1, stack, res)
            stack.pop()
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        self.recur(n,0,0,stack,res)
        return res