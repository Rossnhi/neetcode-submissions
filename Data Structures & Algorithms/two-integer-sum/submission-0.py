class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumHash = {}
        for i in range(len(nums)):
            if target - nums[i] in sumHash:
                return [sumHash[target - nums[i]], i]
            sumHash[nums[i]] = i;
        
        