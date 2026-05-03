class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        greatestToRight = [0] * len(nums)
        greatestToLeft = [0] * len(nums)
        for i in range(len(nums)):
            if i % k == 0:
                greatestToLeft[i] = nums[i]
            else:
                greatestToLeft[i] = max(nums[i], greatestToLeft[i - 1])
            if (len(nums) - i) % k == 0:
                greatestToRight[-i - 1] = nums[-i - 1]
            else:
                greatestToRight[-i - 1] = max(nums[-i - 1], greatestToRight[-i])
        res = [0] * (len(nums) - k + 1)
        for i in range(len(nums) - k + 1):
            res[i] = max(greatestToRight[i], greatestToLeft[i + k - 1])
        return res