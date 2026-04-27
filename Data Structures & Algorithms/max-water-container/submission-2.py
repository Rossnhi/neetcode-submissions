class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            maxWater = max(maxWater, (j - i) * min(heights[i], heights[j]))
            if heights[i] < heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
                j -= 1
        return maxWater