class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = 0
        b = len(nums) - 1
        while a <= b:
            mid = int((a + b)/2)
            print(a, b, mid)
            if target < nums[mid]:
                b = mid - 1
            elif target > nums[mid]:
                a = mid + 1
            else:
                return mid
        else:
            return -1