class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for n in s:
            if n == ')':
                if len(stack) != 0:
                    temp = stack.pop()
                else:
                    return False
                if temp != '(':
                    return False
            elif n == '}':
                if len(stack) != 0:
                    temp = stack.pop()
                else:
                    return False
                if temp != '{':
                    return False
            elif n == ']':
                if len(stack) != 0:
                    temp = stack.pop()
                else:
                    return False
                if temp != '[':
                    return False
            else:
                stack.append(n)
        
        if len(stack) == 0:
            return True
        return False

        