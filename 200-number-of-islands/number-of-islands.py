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

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while q:
                row, col = q.popleft()
                for i, j in directions:
                    r, c = row + i, col + j
                    if (r) in range(rows) and (c) in range(cols) and grid[r][c] == '1' and (r, c) not in seen:
                        q.append((r, c))
                        seen.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in seen:
                    bfs(r, c)
                    numIslands += 1
        return numIslands