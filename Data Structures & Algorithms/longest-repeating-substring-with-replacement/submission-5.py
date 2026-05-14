class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        l = 0
        longest = 0
        windowFreq = defaultdict(int)
        for r in range(len(s)):
            windowFreq[s[r]] += 1
            maxf = max(maxf, windowFreq[s[r]])
            while r - l + 1 - maxf > k:
                windowFreq[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest