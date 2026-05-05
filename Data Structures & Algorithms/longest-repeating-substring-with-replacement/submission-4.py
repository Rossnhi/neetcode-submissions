class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        ch = ""
        windowCount = defaultdict(int)
        l = 0
        for r in range(len(s)):
            print(l, r)
            windowCount[s[r]] += 1
            if windowCount[s[r]] > windowCount[ch]:
                ch = s[r]
            if r - l + 1 - windowCount[ch] <= k:
                res = max(res, r - l + 1)
            else:
                h = windowCount[ch]
                while r - l + 1 - h > k:
                    windowCount[s[l]] -= 1
                    l += 1
        return res