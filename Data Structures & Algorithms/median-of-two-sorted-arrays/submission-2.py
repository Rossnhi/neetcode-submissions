class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1
        b = nums2
        half = (len(a) + len(b)) // 2
        if len(b) < len(a):
            a, b, = b, a
        l = 0
        r = len(a) - 1
        while True:
            m = (l + r)//2
            n = half - m - 2
            aLeft = a[m] if m >= 0 else -math.inf
            aRight = a[m + 1] if m < len(a) - 1 else math.inf
            bLeft = b[n] if n >= 0 else -math.inf
            bRight = b[n + 1] if n < len(b) - 1 else math.inf
            if aLeft > bRight:
                r = m - 1
            elif bLeft > aRight:
                l = m + 1
            else:
                if (len(a) + len(b)) % 2 == 0:
                    return (max(aLeft, bLeft) + min(aRight, bRight))/2
                return min(aRight, bRight)