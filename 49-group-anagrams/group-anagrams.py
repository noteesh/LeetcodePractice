class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {[aet, [eat, tea]]}

        hs = defaultdict(list)

        for n in strs:
            hs[tuple(sorted(n))].append(n)
        
        return list(hs.values())
