class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        nextSmallToRight = [len(heights)] * len(heights)
        nextSmallToLeft = [-1] * len(heights)
        stack = []
        for i in range(len(heights)):
            while len(stack) > 0 and heights[stack[-1]] > heights[i]:
                nextSmallToRight[stack.pop()] = i
            stack.append(i)
        stack = []
        for i in range(len(heights) - 1, -1, -1):
            while len(stack) > 0 and heights[stack[-1]] > heights[i]:
                nextSmallToLeft[stack.pop()] = i
            stack.append(i)
        print(nextSmallToLeft, nextSmallToRight)
        res = 0
        for i in range(len(heights)):
            res = max(res, (nextSmallToRight[i] - nextSmallToLeft[i] - 1) * heights[i])
        return res