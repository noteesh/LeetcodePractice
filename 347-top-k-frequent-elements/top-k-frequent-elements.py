class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        l = [[] for i in range(len(nums) + 1)]

        for n in nums:
            if n in hm:
                hm[n] += 1
            else:
                hm[n] = 1
        
        for key, v in hm.items():
            l[v].append(key)
        
        ret = []
        for i in range(len(l) - 1, 0, -1):
            for n in l[i]:
                ret.append(n)
                if len(ret) == k:
                    return ret
        return ret