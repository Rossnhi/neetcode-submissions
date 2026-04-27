class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        l = 1
        r = maxPile
        while l < r:
            m = (l + r)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/m)
            if hours > h:
                l = m + 1
            else:
                r = m
        return r