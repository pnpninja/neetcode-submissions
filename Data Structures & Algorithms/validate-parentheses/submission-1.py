class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match_map = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        for ch in s:
            match ch:
                case '(' | '{' | '[':
                    stack.append(ch)
                case _:
                    if len(stack) == 0:
                        return False
                    if stack[-1] == match_map[ch]:
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0