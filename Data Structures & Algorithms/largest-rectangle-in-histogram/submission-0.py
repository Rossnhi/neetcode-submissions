class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        nextSmall = [len(heights) for _ in range(len(heights))]
        prevSmall = [-1 for _ in range(len(heights))]
        stack = []
        for i in range(len(heights)):
            while len(stack) != 0 and heights[stack[-1]] > heights[i]:
                nextSmall[stack.pop()] = i
            stack.append(i)
        stack = []
        for i in range(len(heights)):
            while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack) != 0:
                prevSmall[i] = stack[-1]
            stack.append(i)
        areaRect = 0
        print(nextSmall, prevSmall)
        for i in range(len(nextSmall)):
            width = nextSmall[i] - prevSmall[i] - 1
            print(heights[i], width)
            height = heights[i]
            area = width * height
            areaRect = max(areaRect, area)
        return areaRect