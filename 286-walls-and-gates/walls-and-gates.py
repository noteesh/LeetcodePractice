class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        
        
        while queue:
            r, c = queue.popleft()

            if r - 1 >= 0 and rooms[r - 1][c] == 2147483647:
                rooms[r - 1][c] = rooms[r][c] + 1 
                queue.append((r - 1, c))
            if c - 1 >= 0 and rooms[r][c - 1] == 2147483647:
                rooms[r][c - 1] = rooms[r][c] + 1 
                queue.append((r, c - 1))
            if r + 1 < rows and rooms[r + 1][c] == 2147483647:
                rooms[r + 1][c] = rooms[r][c] + 1 
                queue.append((r + 1, c))
            if c + 1 < cols and rooms[r][c + 1] == 2147483647:
                rooms[r][c + 1] = rooms[r][c] + 1 
                queue.append((r, c + 1))