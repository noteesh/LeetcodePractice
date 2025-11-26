class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = min(len(word1), len(word2))
        ret = ''
        for i in range(length):
            ret += word1[i] + word2[i]
        ret += word1[length:] + word2[length:]
        return ret