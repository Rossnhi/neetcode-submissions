class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        leftProd = [1] * len(nums)
        rightProd = [1] * len(nums)
        for i in range(1, len(nums)):
                leftProd[i] = leftProd[i - 1] * nums[i - 1]
                rightProd[-i - 1] = rightProd[-i] * nums[-i]
        for i in range(len(nums)):
            output[i] = leftProd[i] * rightProd[i]
        return output