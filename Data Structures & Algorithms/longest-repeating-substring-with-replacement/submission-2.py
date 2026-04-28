class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        chars = {s[0] : 1}
        res = 1
        c = 1
        for r in range(1, len(s)):
            if s[r] in chars:
                chars[s[r]] += 1
            else:
                chars[s[r]] = 1
            if chars[s[r]] > c:
                c = chars[s[r]]
            while r - l + 1 - c > k:
                chars[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res