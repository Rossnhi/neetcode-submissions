class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        charsInWindow = set()
        l = 0
        for r in range(len(s)):
            while s[r] in charsInWindow:
                charsInWindow.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            charsInWindow.add(s[r])
        return res