class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = []
        prefixProd = 1
        suffixProd = 1
        for i in range(len(nums) - 1):
            prefixProd *= nums[i]
            prefix.append(prefixProd)
        for i in range(len(nums) - 1, 0, -1):
            suffixProd *= nums[i]
            suffix.insert(0, suffixProd)
        suffix.append(1)
        out = []
        for i in range(len(prefix)):
            out.append(prefix[i] * suffix[i])
        return out