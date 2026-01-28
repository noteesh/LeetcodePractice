class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = sorted(s)
        ts = sorted(t)
        return ss == ts