class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []

        def paths(open, close, path):
            nonlocal ret
            nonlocal n

            if len(path) == n*2:
                ret.append(path)

            if open < n:
                path += '('
                paths(open + 1, close, path)
                path = path[:-1]
            
            if close < open:
                path += ')'
                paths(open, close + 1, path)
                path = path[:-1]

        paths(1, 0, "(")
        return ret