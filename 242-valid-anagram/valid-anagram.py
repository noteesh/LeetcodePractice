class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hs = {}

        for i, n in enumerate(s):
            if n in hs:
                hs[n] += 1
            else:
                hs[n] = 1
        
        for i, n in enumerate(t):
            if n not in hs or hs[n] <= 0:
                return False
            else:
                hs[n] -= 1
        
        return True