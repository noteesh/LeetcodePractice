class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, n in enumerate(nums):
            ans = target - n
            if ans in hm:
                return [hm[ans], i]
            hm[n] = i