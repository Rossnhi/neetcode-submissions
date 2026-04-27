class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) * len(matrix[0]) - 1
        while l <= r:
            mid = l + int((r - l)/2)
            if target == matrix[mid // len(matrix[0])][mid % len(matrix[0])]:
                return True
            elif target > matrix[mid // len(matrix[0])][mid % len(matrix[0])]:
                l = mid + 1
            else:
                r = mid - 1
        return False