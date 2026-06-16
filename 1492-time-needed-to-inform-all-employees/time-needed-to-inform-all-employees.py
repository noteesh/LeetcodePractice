class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        hierarchy = defaultdict(list)
        for i, n in enumerate(manager):
            hierarchy[n].append(i)
        
        def dfs(node, time):
            if not hierarchy[node]:
                return time
            return max(dfs(n, time + informTime[node]) for n in hierarchy[node])
        
        return dfs(headID, 0)