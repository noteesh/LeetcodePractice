class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []


        def paths(path, start):
            
            ret.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                paths(path, i + 1)
                path.pop()
        
        paths([], 0)
        return ret