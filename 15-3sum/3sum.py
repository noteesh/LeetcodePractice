class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        s = sorted(nums)
        ret = []

        for i, n in enumerate(s):
            l = i + 1
            r = len(nums) - 1
            target = -1 * n

            if i > 0 and s[i] == s[i - 1]:
                continue

            while l < r:
                if l == i:
                    l += 1
                elif r == i:
                    r -= 1
                
                if s[l] + s[r] == target:
                    ret.append([n, s[l], s[r]])
                    l += 1
                    r -= 1
                    while l < r and s[l] == s[l - 1]:
                        l += 1
                    while l < r and s[r] == s[r + 1]:
                        r -= 1
                elif s[l] + s[r] > target:
                    r -= 1
                elif s[l] + s[r] < target:
                    l += 1
        
        return ret
