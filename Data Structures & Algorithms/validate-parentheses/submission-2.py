class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        for chr in s:
            match chr:
                case '(' | '[' | '{':
                    stack.append(chr)
                case ')' | ']' | '}':
                    exp = map[chr]
                    if not stack or stack[-1] != exp:
                        return False
                    stack.pop()
        return len(stack) == 0
                    

