class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        longestDict = {}
        for num in nums:
            if num in longestDict:
                longestDict[num + 1] = longestDict[num] + 1
                del longestDict[num]
            else:
                if num + 1 not in longestDict:
                    longestDict[num + 1] = 1
        maxLength = 0
        for num in longestDict:
            if longestDict[num] > maxLength:
                maxLength = longestDict[num]
        return maxLength