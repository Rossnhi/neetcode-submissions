class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        waterStack = []
        for i in range(len(height)):
            while len(waterStack) > 0 and height[waterStack[-1]] < height[i]:
                bottom = waterStack.pop()
                if len(waterStack) == 0:
                    continue
                left = waterStack[-1]
                h = min(height[left], height[i]) - height[bottom]
                water += h * (i - left - 1)
            waterStack.append(i)
        return water