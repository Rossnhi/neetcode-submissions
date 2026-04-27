class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        pivot = None
        while l <= r:
            m = l + int((r - l)/2)
            if nums[l] > nums[m]:
                l += 1
                r = m
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                pivot = l
                break
        print(pivot)
        s1 = self.binarySearch(nums[pivot:], target)
        s2 = self.binarySearch(nums[:pivot], target)
        if s1 != -1:
            return pivot + s1
        if s2 != -1:
            return s2
        return -1

    def binarySearch(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + int((r - l)/2)
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return -1