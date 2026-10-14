class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        hs = {}
        for i in range(numCourses):
            hs[i] = []
        for i, j in prerequisites:
            hs[i].append(j)
        
        completed = set()
        def dfs(crs):
            if crs in completed:
                return False
            if len(hs[crs]) == 0:
                return True
            
            completed.add(crs)
            for n in hs[crs]:
                if not dfs(n):
                    return False
            completed.remove(crs)
            hs[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True