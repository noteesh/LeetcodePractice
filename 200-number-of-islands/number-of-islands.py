class Solution:
    from collections import deque
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        numIslands = 0

        def bfs(r, c):


            q = deque()
            seen.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                if (row + 1) in range(rows) and (col) in range(cols) and grid[row + 1][col] == '1' and (row + 1, col) not in seen:
                    q.append((row + 1, col))
                    seen.add((row + 1, col))
                if (row - 1) in range(rows) and (col) in range(cols) and grid[row - 1][col] == '1' and (row - 1, col) not in seen:
                    q.append((row - 1, col))
                    seen.add((row - 1, col))
                if (row) in range(rows) and (col + 1) in range(cols) and grid[row][col + 1] == '1' and (row, col + 1) not in seen:
                    q.append((row, col + 1))
                    seen.add((row, col + 1))
                if (row) in range(rows) and (col - 1) in range(cols) and grid[row][col - 1] == '1' and (row, col - 1) not in seen:
                    q.append((row, col - 1))
                    seen.add((row, col - 1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in seen:
                    bfs(r, c)
                    numIslands += 1
        return numIslands