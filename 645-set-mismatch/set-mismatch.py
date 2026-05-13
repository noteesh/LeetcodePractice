class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        double = -1
        missing = -1
        s = set()

        for n in nums:
            if n not in s:
                s.add(n)
            else:
                double = n
                break

        for i in range(1, len(nums) + 1):
            if i not in nums:
                missing = i
                break
        
        return [double, missing]