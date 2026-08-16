class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '*':
                last_num = stack.pop()
                stack[-1] = stack[-1] * last_num
            elif token == '/':
                last_num = stack.pop()
                stack[-1] = int(stack[-1] / last_num)
            elif token == '+':
                last_num = stack.pop()
                stack[-1] = stack[-1] + last_num
            elif token == '-':
                last_num = stack.pop()
                stack[-1] = stack[-1] - last_num
            else:
                stack.append(int(token))
        return stack[-1]