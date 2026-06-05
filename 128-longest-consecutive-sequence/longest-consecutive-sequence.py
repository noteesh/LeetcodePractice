class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ret = 0
        s = set(nums)
        
        highest = 0
        
        for n in s:
            if n - 1 not in s:
                highest = 1
                temp = n

                while temp + 1 in s:
                    temp += 1
                    highest += 1

                if highest > ret:
                    ret = highest
        
        return ret
                