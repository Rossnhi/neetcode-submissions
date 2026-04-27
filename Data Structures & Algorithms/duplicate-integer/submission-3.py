class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = {}
        for num in nums:
            if num in numSet:
                return True
            else:
                numSet[num] = False
        return False