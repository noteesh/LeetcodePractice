class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        seen = set()
        rows, cols = len(board), len(board[0])

        def bfs(r, c):
            q = []
            q.append((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while q:
                row, col = q.pop()
                for i, j in directions:
                    r, c = row + i, col + j
                    if r in range(rows) and c in range(cols) and board[r][c] == "O" and (r, c) not in seen:
                        seen.add((r, c))
                        q.append((r, c))


        for r in range(rows):
            if board[r][0] == "O" and (r, 0) not in seen:
                bfs(r, 0)
                seen.add((r, 0))
            if board[r][cols - 1] == "O" and (r, cols - 1) not in seen:
                bfs(r, cols - 1)
                seen.add((r, cols - 1))
        for c in range(cols):
            if board[0][c] == "O" and (0, c) not in seen:
                bfs(0, c)
                seen.add((0, c))
            if board[rows - 1][c] == "O" and (rows - 1, c) not in seen:
                bfs(rows - 1, c)
                seen.add((rows - 1, c))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in seen:
                    board[r][c] = "X"