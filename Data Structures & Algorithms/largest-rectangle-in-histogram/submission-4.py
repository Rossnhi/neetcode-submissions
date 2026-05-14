class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        smallerToRight = [len(heights)] * len(heights)
        smallerToLeft = [-1] * len(heights)
        stack = []
        for i in range(len(heights)):
            while len(stack) and heights[stack[-1]] > heights[i]:
                smallerToRight[stack.pop()] = i
            stack.append(i)
        stack = []
        for i in range(len(heights)):
            while len(stack) and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack):
                smallerToLeft[i] = stack[-1]
            stack.append(i)
        rect = 0
        for i in range(len(heights)):
            rect = max(rect, heights[i] * (smallerToRight[i] - smallerToLeft[i] - 1))
        return rect