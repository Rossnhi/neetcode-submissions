class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = (len(matrix) * len(matrix[0])) - 1
        while l <= r:
            m = l + int((r - l)/2)
            if matrix[m // len(matrix[0])][m % len(matrix[0])] == target:
                return True
            elif matrix[m // len(matrix[0])][m % len(matrix[0])] < target:
                l = m + 1
            else:
                r = m - 1
        return False