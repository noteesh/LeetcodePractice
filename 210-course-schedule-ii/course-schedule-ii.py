class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        hs = {}
        for i in range(numCourses):
            hs[i] = []
        for i, j in prerequisites:
            hs[i].append(j)
        ret = []
        seen = set()
        visited = set()
        def dfs(n):
            if n in seen:
                return False
            if n in visited:
                return True
            
            seen.add(n)
            for m in hs[n]:
                if not dfs(m):
                    return False
            seen.remove(n)
            visited.add(n)
            ret.append(n)
            hs[n] = []
            return True



        for n in range(numCourses):  
            if not dfs(n):
                return []

        return ret