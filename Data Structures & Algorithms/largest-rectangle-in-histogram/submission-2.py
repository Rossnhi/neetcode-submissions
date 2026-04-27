class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left = [-1 for _ in range(len(heights))]
        stack = []
        for i in range(len(heights)):
            while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack) != 0:
                left[i] = stack[-1]
            stack.append(i)
        right = [len(heights) for _ in range(len(heights))]
        stack = []
        for i in range(len(heights)):
            while len(stack) != 0 and heights[stack[-1]] > heights[i]:
                right[stack.pop()] = i
            stack.append(i)
        maxRect = 0
        for i in range(len(heights)):
            area = heights[i] * (right[i] - left[i] - 1)
            maxRect = max(maxRect, area)
        return maxRect