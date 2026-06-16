class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]



        def bfs(r, c):
            queue = deque()
            seen = set()
            queue.append((r, c))
            seen.add((r, c))

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and heights[nr][nc] >= heights[row][col] and (nr, nc) not in seen:
                        queue.append((nr, nc))
                        seen.add((nr, nc))
            
            return seen
        
        pacificSet = set()
        atlanticSet = set()

        for i in range(cols):
            pacificSet = pacificSet.union(bfs(0, i))
        for j in range(rows):
            pacificSet = pacificSet.union(bfs(j, 0))

        for i in range(cols):
            atlanticSet = atlanticSet.union(bfs(rows - 1, i))
        for j in range(rows):
            atlanticSet = atlanticSet.union(bfs(j, cols - 1))

        return list(pacificSet.intersection(atlanticSet))

