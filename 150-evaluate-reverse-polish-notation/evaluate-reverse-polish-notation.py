class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for n in tokens:
            if n == '+':
                temp = int(stack.pop()) + int(stack.pop())
                stack.append(temp)
            elif n == '-':
                a = int(stack.pop())
                b = int(stack.pop())
                temp = b - a
                stack.append(temp)
            elif n == '*':
                temp = int(stack.pop()) * int(stack.pop())
                stack.append(temp)
            elif n == "/":
                a = int(stack.pop())
                b = int(stack.pop())
                temp = b / a
                stack.append(temp)
            else:
                stack.append(n)
        return int(stack.pop())
        