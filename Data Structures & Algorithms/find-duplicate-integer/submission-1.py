class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            print(num)
            n = num
            if num > len(nums):
                n = num - len(nums)
            if nums[n] > len(nums):
                return n
            else:
                nums[n] += len(nums)