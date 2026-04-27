class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = 0
        b = len(nums) - 1
        while b - a > 1:
            mid = int((a + b)/2)
            print(a, b, mid)
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                b = mid
            else:
                a = mid
        if target == nums[a]:
            return a
        elif target == nums[b]:
            return b
        else:
            return -1