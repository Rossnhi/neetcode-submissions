class Solution:
    def binarySearch(self, l : int, r : int, nums : List[int], target : int):
        if l > r:
            return -1
        mid = l + int((r - l)/2)
        if target > nums[mid]:
            return self.binarySearch(mid + 1, r, nums, target)
        elif target < nums[mid]:
            return self.binarySearch(l, mid - 1, nums, target)
        else:
            return mid
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(0, len(nums) - 1, nums, target)