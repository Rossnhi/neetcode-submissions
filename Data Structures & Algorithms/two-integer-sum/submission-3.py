class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = {}
        for i in range(len(nums)):
            if nums[i] in numSet:
                return [numSet[nums[i]], i]
            else:
                numSet[target - nums[i]] = i