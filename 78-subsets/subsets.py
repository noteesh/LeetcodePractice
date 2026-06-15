class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        ret = []


        def paths(start, path):
            nonlocal nums
            nonlocal ret

            ret.append(path[:])
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                paths(i + 1, path)
                path.pop()


        paths(0, [])
        return ret



        