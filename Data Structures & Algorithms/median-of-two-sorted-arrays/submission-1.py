class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1
        b = nums2
        if len(a) > len(b):
            a,b = b,a
        target = (len(a) + len(b))// 2
        l = 0
        r = len(a) - 1
        while True:
            m = (l + r)//2
            n = target - m - 2
            aLeft = a[m] if m >= 0 else -math.inf
            aRight = a[m + 1] if m < len(a) - 1 else math.inf
            bLeft = b[n] if n >= 0 else -math.inf
            bRight = b[n + 1] if n < len(b) - 1 else math.inf
            if bLeft > aRight:
                l = m + 1
            elif aLeft > bRight:
                r = m - 1
            else:
                if (len(a) + len(b)) % 2 == 0:
                    return (max(aLeft, bLeft) + min(aRight, bRight))/2
                return min(aRight, bRight) 