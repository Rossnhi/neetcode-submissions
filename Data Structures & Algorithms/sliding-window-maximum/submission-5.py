class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [0] * (len(nums) - k + 1)
        right = [0] * len(nums)
        left = [0] * len(nums)
        for i in range(len(nums)):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
        for i in range(-1, -len(nums) - 1, -1):
            if i == -1 or (len(nums) + i + 1) % k == 0:
                right[i] = nums[i]
            else:
                right[i] = max(right[i + 1], nums[i])
        for i in range(len(nums) - k + 1):
            res[i] = max(right[i], left[i + k - 1])
        return res