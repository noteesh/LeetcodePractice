class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        hs = {}
        for i in range(numCourses):
            hs[i] = []
        for i, j in prerequisites:
            hs[i].append(j)
        
        seen = set()
        def dfs(n):
            if len(hs[n]) == 0:
                return True
            if n in seen:
                return False
            
            seen.add(n)
            for m in hs[n]:
                if not dfs(m):
                    return False
            seen.remove(n)
            hs[n] = []
            return True



        for n in range(numCourses):
            if not dfs(n):
                return False

        return True