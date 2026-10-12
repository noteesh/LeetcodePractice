class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        ret = []

        candidates.sort()

        def paths(start, path):
            tempSum = sum(path)
            if tempSum == target:
                ret.append(path[:])
            
            targetLeft = target - tempSum

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] <= targetLeft:
                    path.append(candidates[i])
                    paths(i + 1, path)
                    path.pop()

        paths(0, [])
        return ret