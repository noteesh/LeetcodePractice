class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_list = sorted(nums)
        ret = []

        target = 0
        for i, n in enumerate(sorted_list):
            if i > 0 and n == sorted_list[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                target = n + sorted_list[left] + sorted_list[right]
                if target == 0:
                    ret.append([n, sorted_list[left], sorted_list[right]])
                    left += 1
                    while left < right and sorted_list[left] == sorted_list[left - 1]:
                        left += 1
                elif target < 0:
                    left += 1
                else:
                    right -= 1
        return ret