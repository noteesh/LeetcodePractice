class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hs = defaultdict(list)
        for word in strs:
            s = ''.join(sorted(word))
            hs[s].append(word)
        return list(hs.values())