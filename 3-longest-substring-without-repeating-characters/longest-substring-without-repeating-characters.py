class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        p2 = 0
        seen = set()
        maxCount = 0
        count = 0

        while p2 <= len(s) - 1:
            if s[p2] in seen:
                if count > maxCount:
                    maxCount = count
                while s[p1] != s[p2]:
                    seen.remove(s[p1])
                    p1 += 1
                    count -= 1
                seen.remove(s[p1])
                p1 += 1
                count -= 1

            else:
                seen.add(s[p2])
                p2 += 1
                count += 1
        
        if count > maxCount:
            maxCount = count
        
        return maxCount
        