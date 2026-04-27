class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxVol = 0
        while(i < j):
            print(i, j, heights[i], heights[j])
            minHeightIndex = i if heights[i] < heights[j] else j
            vol = (j - i) * heights[minHeightIndex]
            maxVol = max(maxVol, vol)
            if i == minHeightIndex:
                i += 1
            else:
                j -= 1
        return maxVol
