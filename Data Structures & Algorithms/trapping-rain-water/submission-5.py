class Solution:
    def trap(self, height: List[int]) -> int:
        greatestToLeft = [] # len(height) - 2
        greatestToRight = [] # len(height) - 2
        for i in range(1, len(height) - 1):
            if i == 1:
                greatestToLeft.append(height[0])
                greatestToRight.append(height[len(height) - 1])
            else:
                greatestToLeft.append(max(height[i - 1], greatestToLeft[-1]))
                greatestToRight.insert(0, max(height[-i], greatestToRight[0]))
        water = 0

        for i in range(1, len(height) - 1):
            minHeight = min(greatestToLeft[i - 1], greatestToRight[i - 1])
            if minHeight > height[i]:
                water += minHeight - height[i]
        return water