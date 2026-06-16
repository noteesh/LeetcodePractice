class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)

        a = 0
        b = 1
        c = 2

        path = [a] * numCourses

        def dfs(crs):
            if path[crs] == b:
                return False
            if path[crs] == c:
                return True
            
            path[crs] = b
            for n in graph[crs]:
                if not dfs(n):
                    return False

            path[crs] = c
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
