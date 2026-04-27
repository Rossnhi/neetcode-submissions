class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r)//2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[l] > nums[m]:
                r = m
                l += 1
            else:
                return nums[l]
        return nums[l]