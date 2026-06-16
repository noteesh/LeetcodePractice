class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()

        def bfs(r, c):
            queue = deque()
            seen.add((r, c))
            queue.append((r, c))
            
            while queue:
                dr, dc = queue.popleft()
                
                if dr + 1 < rows and grid[dr + 1][dc] == '1' and (dr + 1, dc) not in seen:
                    seen.add((dr + 1, dc))
                    queue.append((dr + 1, dc))
                    bfs(dr + 1, dc)
                if dr - 1 >= 0 and grid[dr - 1][dc] == '1' and (dr - 1, dc) not in seen:
                    seen.add((dr - 1, dc))
                    queue.append((dr - 1, dc))
                    bfs(dr - 1, dc)
                if dc + 1 < cols and grid[dr][dc + 1] == '1' and (dr, dc + 1) not in seen:
                    seen.add((dr, dc + 1))
                    queue.append((dr, dc + 1))
                    bfs(dr, dc + 1)
                if dc - 1 >= 0 and grid[dr][dc - 1] == '1' and (dr, dc - 1) not in seen:
                    seen.add((dr, dc - 1))
                    queue.append((dr, dc - 1))
                    bfs(dr, dc - 1)
                



        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in seen:
                    bfs(i, j)
                    count += 1

        return count