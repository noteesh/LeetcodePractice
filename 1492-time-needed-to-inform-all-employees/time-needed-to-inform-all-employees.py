class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # build adjacency list: manager -> list of subordinates
        sub = defaultdict(list)
        for emp, mgr in enumerate(manager):
            if mgr != -1:
                sub[mgr].append(emp)
    
        # dfs returns max time to inform everyone in this subtree
        def dfs(node, time):
            if not sub[node]:        # leaf node, no subordinates
                return time
            return max(dfs(child, time + informTime[node]) for child in sub[node])
    
        return dfs(headID, 0)