class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[] for _ in range(2 ** len(nums))]
        isInSet = True
        for i in range(len(nums)):
            for j in range(len(subsets)):
                if j % (2 ** i) == 0:
                    isInSet = not isInSet
                if isInSet:
                    subsets[j].append(nums[i])
        return subsets