class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        maxLeft = 0
        maxRight = 0
        i = 0
        j = len(height) - 1
        while i <= j:
            print(i, maxLeft, j, maxRight, water)
            if maxLeft <= maxRight:
                water += max(0, maxLeft - height[i])
                maxLeft = max(maxLeft, height[i])
                i += 1
            else:
                water += max(0, maxRight - height[j])
                maxRight = max(maxRight, height[j])
                j -= 1
        return water