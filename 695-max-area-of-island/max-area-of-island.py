class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
        
        seen = set()
        maxArea = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            seen.add((r, c))
            q.append((r, c))
            temp = 1

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while q:
                row, col = q.popleft()
                for i, j in directions:
                    r, c = row + i, col + j
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in seen:
                        q.append((r, c))
                        seen.add((r, c))
                        temp += 1
                        
            nonlocal maxArea
            if temp > maxArea:
                maxArea = temp
                

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    bfs(r, c)
        
        return maxArea




        