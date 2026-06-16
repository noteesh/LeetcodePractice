class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        hierarchy = defaultdict(list)

        for i, n in enumerate(manager):
            hierarchy[n].append(i)

        st = []
        count = 0
        st.append((headID, 0))
        maxCount = 0

        while st:
            temp, count = st.pop()
            maxCount = max(maxCount, count)

            for n in hierarchy[temp]:
                st.append((n, count + informTime[temp]))
        
        return maxCount