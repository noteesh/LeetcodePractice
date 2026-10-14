class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        rotten = 0
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2 :
                    q.append((r, c))
                    seen.add((r, c))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for i, j in directions:
                    r, c = row + i, col + j
                    if r in range(rows) and c in range(cols) and (r, c) not in seen and grid[r][c] == 1:
                        q.append((r, c))
                        seen.add((r, c))
                        grid[r][c] = 2
            rotten += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return rotten - 1 if rotten > 0 else 0