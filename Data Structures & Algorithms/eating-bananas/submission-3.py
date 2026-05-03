class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        kMax = max(piles)
        l = 1
        r = kMax
        while l < r:
            m = (l + r)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / m)
            if hours <= h:
                r = m
            else:
                l = m + 1
        return l