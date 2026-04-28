class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        chars = {s[0] : 1}
        res = 1
        c = s[0]
        for r in range(1, len(s)):
            print(l, r, c, res)
            if s[r] == c:
                chars[c] += 1
                res = max(res, r - l + 1)
            else:
                if s[r] in chars:
                    chars[s[r]] += 1
                else:
                    chars[s[r]] = 1
                for ch in chars:
                    if chars[ch] > chars[c]:
                        c = ch
                if r - l + 1 - chars[c] <= k:
                    res = max(res, r - l + 1)
                else:
                    while True:
                        chars[s[l]] -= 1
                        l += 1
                        for ch in chars:
                            if chars[ch] > chars[c]:
                                c = ch
                        if r - l + 1 - chars[c] <= k:
                            break
        return res