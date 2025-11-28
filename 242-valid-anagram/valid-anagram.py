class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        prev solution:

        if len(s) != len(t):
            return False
        hs = {}
        for i, n in enumerate(s):
            if n in hs:
                hs[n] += 1
            else:
                hs[n] = 1
        for i, n in enumerate(t):
            if n in hs and hs[n] > 0:
                hs[n] -= 1
            else:
                return False
        return True
        '''
        sortS = sorted(s)
        sortT = sorted(t)
        return sortS == sortT