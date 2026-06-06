class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        mid = 0
        rightRow = []

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                l = 0
                r = len(matrix[mid]) - 1
                m = 0

                while l <= r:
                    m = (l + r) // 2

                    if matrix[mid][m] == target:
                        return True
                    elif r == l:
                        return False
                    elif matrix[mid][m] > target:
                        r = m - 1
                    else:
                        l = m + 1

                return False
            elif left == right:
                return False
            elif matrix[mid][0] > target:
                right = mid - 1

            elif matrix[mid][-1] < target:
                left = mid + 1
        return False