class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # {[2, 0], [7, 1], ...}

        hs = {}

        for i, n in enumerate(nums):
            if target - n in hs:
                return [i, hs[target - n]]
            else:
                hs[n] = i
        
        return -1