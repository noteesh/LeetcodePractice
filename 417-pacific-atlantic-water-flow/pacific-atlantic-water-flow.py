class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])
        pset = set()
        aset = set()

        def bfs(r, c):
            q = collections.deque()
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            seen = set()
            seen.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                for i, j in directions:
                    r, c = row + i, col + j
                    if r in range(rows) and c in range(cols) and heights[r][c] >= heights[row][col] and (r, c) not in seen:
                        seen.add((r, c))
                        q.append((r, c))
            return seen

        for i in range(rows):
            pset = pset.union(bfs(i, 0))
        for j in range(cols):
            pset = pset.union(bfs(0, j))
        
        for i in range(rows):
            aset = aset.union(bfs(i, cols - 1))
        for j in range(cols):
            aset = aset.union(bfs(rows - 1, j))
        
        return list(pset.intersection(aset))
