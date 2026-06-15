class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        def paths(start, path):
            nonlocal target
            nonlocal ret
            nonlocal candidates

            sumSoFar = sum(path)
            if sumSoFar == target:
                ret.append(path[:])

            targetLeft = target - sumSoFar

            for i in range(start, len(candidates)):
                if candidates[i] <= targetLeft:
                    path.append(candidates[i])
                    paths(i, path)
                    path.pop()
            
        paths(0, [])
        return ret