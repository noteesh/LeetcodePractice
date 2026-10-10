class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        st = []

        ret = [0] * len(temperatures)

        for i, n in enumerate(temperatures):
            if not st:
                st.append(i)
                continue
            
            while st and n > temperatures[st[-1]]:
                idx = st.pop()
                ret[idx] = i - idx

            st.append(i)
        return ret
                

        