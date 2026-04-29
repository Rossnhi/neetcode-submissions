class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        leftMax = [0] * len(nums)
        rightMax = [0] * len(nums)
        for i in range(len(nums)):
            if i % k == 0:
                leftMax[i] = nums[i]
            else:
                leftMax[i] = max(nums[i], leftMax[i - 1])
            if (len(nums) - i) % k == 0 or i == 0:
                rightMax[-i - 1] = nums[-i - 1]
            else:
                rightMax[-i - 1] = max(nums[-i - 1], rightMax[-i])
        print(leftMax, rightMax)
        res = [0] * (len(nums) - k + 1)
        for i in range(len(nums) - k + 1):
            res[i] = max(rightMax[i], leftMax[i + k - 1])
        return res