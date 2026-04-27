class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        for i in range(len(nums) - 1):
            prefix.append(prefix[i] * nums[i])
        for i in range(len(nums) - 1, 0, -1):
            suffix.insert(0, suffix[0] * nums[i])
        out = []
        print(prefix, suffix)
        for i in range(len(prefix)):
            out.append(prefix[i] * suffix[i])
        return out