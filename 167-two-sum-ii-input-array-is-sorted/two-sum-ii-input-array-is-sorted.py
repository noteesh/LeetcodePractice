class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        hs = {}

        for i, n in enumerate(numbers):
            if target - n in hs:
                return [hs[target - n] + 1, i + 1]
            else:
                hs[n] = i
        