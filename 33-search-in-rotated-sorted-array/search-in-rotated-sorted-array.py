class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = 0
        leftSorted = True
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:
                leftSorted = True
            else:
                leftSorted = False

            if leftSorted and target >= nums[left] and target <= nums[mid]:
                right = mid - 1
            elif not leftSorted and target >= nums[mid] and target <= nums[right]:
                left = mid + 1
            elif leftSorted:
                left = mid + 1
            elif not leftSorted:
                right = mid - 1
        return -1