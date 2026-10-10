class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) //2

            if nums[l] <= nums[r]:
                return nums[l]
            elif nums[m] < nums[l]:
                r = m
            elif nums[m] > nums[r]:
                l = m + 1
        return -1

        