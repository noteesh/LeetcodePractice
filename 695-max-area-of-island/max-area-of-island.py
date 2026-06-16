class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        maxArea = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            seen.add((r, c))
            curArea = 1
            nonlocal maxArea

            while queue:
                row, col = queue.popleft()

                if row - 1 >= 0 and grid[row - 1][col] == 1 and (row - 1, col) not in seen:
                    seen.add((row - 1, col))
                    queue.append((row - 1, col))
                    curArea += 1
                if col + 1 < cols and grid[row][col + 1] == 1 and (row, col + 1) not in seen:
                    seen.add((row, col + 1))
                    queue.append((row, col + 1))
                    curArea += 1
                if row + 1 < rows and grid[row + 1][col] == 1 and (row + 1, col) not in seen:
                    seen.add((row + 1, col))
                    queue.append((row + 1, col))
                    curArea += 1
                if col - 1 >= 0 and grid[row][col - 1] == 1 and (row, col - 1) not in seen:
                    seen.add((row, col - 1))
                    queue.append((row, col - 1))
                    curArea += 1
            
            if curArea > maxArea:
                maxArea = curArea

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in seen:
                    bfs(i, j)
        
        return maxArea