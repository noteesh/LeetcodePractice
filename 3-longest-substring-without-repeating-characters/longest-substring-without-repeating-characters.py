class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        p2 = 0
        charCheck = set()
        curMax = 0

        while p2 <= len(s) - 1:
            if s[p2] not in charCheck:
                charCheck.add(s[p2])
                p2 += 1
            elif s[p2] in charCheck:
                while s[p2] in charCheck:
                    temp = s[p1]
                    p1 += 1
                    charCheck.remove(temp)
                charCheck.add(s[p2])
                p2 += 1
                
            if len(charCheck) > curMax:
                curMax = len(charCheck)
        
        return curMax