class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ret = []

        def backtrack(start, path):
            tempSum = sum(path)
            if tempSum == target:
                ret.append(path[:])

            targetLeft = target - tempSum
            
            for i in range(start, len(candidates)):
                if candidates[i] <= targetLeft:
                    path.append(candidates[i])
                    backtrack(i, path)
                    path.pop()

        backtrack(0, [])        
        return ret