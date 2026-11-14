class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case "+" | "-" | "*" | "/":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    if token == "+":
                        stack.append(num1 + num2)
                    elif token == "*":
                        stack.append(num1 * num2)
                    elif token == "-":
                        stack.append(num1 - num2)
                    else:
                        if num2 == 0:
                            stack.append(0)
                        else:
                            stack.append(int(num1 / num2))
                case _:
                    stack.append(int(token))
        return stack.pop()
