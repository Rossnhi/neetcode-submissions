class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        charsSeen = {s[0] : 0}
        longest = 1
        l = 0
        r = 0
        subStrLen = 1
        while l <= r and r < len(s) - 1:
            print(charsSeen, l, r)
            if s[r + 1] not in charsSeen:
                r += 1
                subStrLen += 1
                charsSeen[s[r]] = r
            else:
                for i in range(l, charsSeen[s[r + 1]]):
                    charsSeen.pop(s[i])
                l = charsSeen[s[r + 1]] + 1
                r += 1
                longest = max(longest, subStrLen)
                subStrLen = r - l + 1
                charsSeen[s[r]] = r
        return max(longest, subStrLen)
                
