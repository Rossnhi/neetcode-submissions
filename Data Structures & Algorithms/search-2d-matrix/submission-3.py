class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = (len(matrix) * len(matrix[0])) - 1
        while l <= r:
            m = (l + r)//2
            if matrix[m // len(matrix[0])][m % len(matrix[0])] < target:
                l = m + 1
            elif matrix[m // len(matrix[0])][m % len(matrix[0])] > target:
                r = m - 1
            else:
                return True
        return False