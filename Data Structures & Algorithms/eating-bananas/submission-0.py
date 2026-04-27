class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles = sorted(piles)
        minRate = 1
        maxRate = max(piles)
        while minRate <= maxRate:
            if minRate == maxRate:
                return minRate
            midRate = minRate + int((maxRate - minRate)/2)
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/midRate)
            if hours > h:
                minRate = midRate + 1
            else:
                maxRate = midRate  