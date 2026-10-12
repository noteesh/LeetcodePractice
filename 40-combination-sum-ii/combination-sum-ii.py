class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []

        candidates.sort()

        def paths(start, path):
            nonlocal candidates
            nonlocal target
            nonlocal ret

            sumSoFar = sum(path)

            if sumSoFar == target:
                ret.append(path[:])
            
            targetLeft = target - sumSoFar
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] <= targetLeft:
                    path.append(candidates[i])
                    paths(i + 1, path)
                    path.pop()

        paths(0, [])
        return ret