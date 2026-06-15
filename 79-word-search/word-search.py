class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def paths(r, c, l):
            if l == len(word):
                return True
            if r >= rows or c >= cols or r < 0 or c < 0 or word[l] != board[r][c] or (r, c) in path:
                return False
            
            path.add((r, c))
            exists = paths(r + 1, c, l + 1) or paths(r - 1, c, l + 1) or paths(r, c + 1, l + 1) or paths(r, c - 1, l + 1)
            path.remove((r, c))

            return exists

        for i in range(rows):
            for j in range(cols):
                if paths(i, j, 0):
                    return True
        return False
