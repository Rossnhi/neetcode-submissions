class Solution:
    def trap(self, height: List[int]) -> int:
        maxToLeft = []
        maxToRight = []
        for i in range(1, len(height) - 1):
            if i == 1:
                maxToLeft.append(height[0])
                maxToRight.append(height[-1])
                continue
            maxToLeft.append(max(maxToLeft[-1], height[i - 1]))
            maxToRight.insert(0, max(maxToRight[0], height[-i]))
        water = 0
        for i in range(1, len(height) - 1):
            if min(maxToLeft[i - 1], maxToRight[i - 1]) - height[i] > 0:
                water += min(maxToLeft[i - 1], maxToRight[i - 1]) - height[i]
        return water