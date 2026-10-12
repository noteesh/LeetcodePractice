class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        ret = []

        nums.sort()

        def paths(start, path):

            ret.append(path[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                paths(i + 1, path)
                path.pop()
        
        paths(0, [])
        return ret