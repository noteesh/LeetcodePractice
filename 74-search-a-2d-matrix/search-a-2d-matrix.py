class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        targetList = -1
        while l <= r:
            m = (l + r) // 2

            if matrix[m][0] == target or matrix[m][-1] == target:
                return True
            elif matrix[m][0] < target and matrix[m][-1] > target:
                targetList = m
                break
            elif matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
        
        ll = 0
        rr = len(matrix[targetList]) - 1

        while ll <= rr:
            m = (ll + rr) // 2
            
            if matrix[targetList][m] == target:
                return True
            elif matrix[targetList][m] > target:
                rr = m - 1
            else:
                ll = m + 1
        
        return False
