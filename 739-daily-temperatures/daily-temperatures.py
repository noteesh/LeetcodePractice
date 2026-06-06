class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        stack = []

        for i, n in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < n:
                prev = stack.pop()
                ret[prev] = i - prev
            stack.append(i)
        return ret