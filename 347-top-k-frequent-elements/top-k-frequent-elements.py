import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
            [1, 1, 1, 2, 2, 3]

            [[], [3], [2], [1], [] ,[] ,[]]
        
        l = [[] for i in range(len(nums) + 1)]
        hs = {}

        for n in nums:
            if n in hs:
                hs[n] += 1
            else:
                hs[n] = 1
        
        for n, c in hs.items():
            l[c].append(n)
        
        ret = []
        for i in range(len(l) - 1, 0, -1):
            for n in l[i]:
                ret.append(n)
                if len(ret) == k:
                    return ret
        return -1
        '''
        if k == 0:
            return []

        hs = {}
        minHeap = []

        for n in nums:
            if n in hs:
                hs[n] += 1
            else:
                hs[n] = 1
        
        for i, n in hs.items():
            heapq.heappush(minHeap, (n, i))

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        ret = []
        for i, n in minHeap:
            ret.append(n)
        return ret

