class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        ret = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while st and temperatures[st[-1]] < temp:
                prev = st.pop()
                ret[prev] = i - prev
            st.append(i)
        return ret