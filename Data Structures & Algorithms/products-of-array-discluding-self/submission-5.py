class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffixProd = 1
        prefixProd = 1
        suffix = [1]
        prefix = [1]
        for i in range(len(nums) - 1):
            prefixProd *= nums[i]
            prefix.append(prefixProd)
        for i in range(len(nums) - 1, 0, -1):
            suffixProd *= nums[i]
            suffix.insert(0, suffixProd)
        out = []
        for n, m in zip(prefix, suffix):
            out.append(n * m)
        return out