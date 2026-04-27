class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        maxLeft = []
        maxRight = []
        for i in range(1, len(height) - 1):
            if i == 1:
                maxLeft.append(height[0])
                maxRight.append(height[-1])
            else:
                maxLeft.append(max(maxLeft[-1], height[i - 1]))
                maxRight.insert(0, max(maxRight[0], height[-i]))
        for i in range(1, len(height) - 1):
            water += max(0, min(maxLeft[i - 1], maxRight[i - 1]) - height[i])
        return water