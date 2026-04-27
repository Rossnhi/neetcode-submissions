class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArr = [1]
        suffixArr = [1]
        for i in range(1 ,len(nums)):
            prefixArr.append(prefixArr[-1] * nums[i - 1])
            suffixArr.insert(0, suffixArr[0] * nums[-i])
        out = []
        for i in range(len(prefixArr)):
            out.append(prefixArr[i] * suffixArr[i])
        return out