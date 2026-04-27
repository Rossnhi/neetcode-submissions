class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = 1
            k = len(nums) - 1
            while i + j < k:
                if nums[i + j] + nums[k] == -nums[i]:
                    triplets.append([nums[i], nums[i + j], nums[k]])
                    j += 1
                    k -= 1
                    while i + j < k and nums[i + j] == nums[i + j - 1]:
                        j += 1
                    while i + j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif nums[i + j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    k -= 1
        return triplets