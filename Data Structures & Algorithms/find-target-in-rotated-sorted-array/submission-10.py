class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            print(l, r, m)
            if target == nums[m]:
                return m
            if nums[l] <= target < nums[m] or (nums[m] < nums[l] and (target < nums[m] or nums[r] < target)):
                r = m - 1
            else:
                l = m + 1
        return l if target == nums[l] else -1