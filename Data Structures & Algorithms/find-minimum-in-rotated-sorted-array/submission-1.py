class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            print(l, r, l + int((r - l)/2))
            if l == r:
                return nums[l]
            m = l + int((r - l)/2)
            if nums[l] > nums[m]:
                r = m
                l += 1
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                return nums[l]