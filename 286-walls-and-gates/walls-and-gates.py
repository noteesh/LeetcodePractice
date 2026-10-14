class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        rows, cols = len(rooms), len(rooms[0])
    
        def bfs(r, c):
            
            q = collections.deque()
            q.append((r, c, 0))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while q:
                row, col, d = q.popleft()
                for i, j in directions:
                    r, c = row + i, col + j

                    if r in range(rows) and c in range(cols) and rooms[r][c] != -1 and rooms[r][c] != 0 and d + 1 < rooms[r][c]:
                        q.append((r, c, d + 1))
                        rooms[r][c] = d + 1



        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    bfs(r, c)
                    
        