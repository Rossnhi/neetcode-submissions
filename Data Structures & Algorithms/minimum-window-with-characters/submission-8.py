class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        if len(s) < len(t):
            return res
        tFreq = defaultdict(int)
        unique = 0
        for ch in t:
            tFreq[ch] += 1
            if tFreq[ch] == 1:
                unique += 1
        windowFreq = defaultdict(int)
        l = 0
        matches = 0
        for r in range(len(s)):
            windowFreq[s[r]] += 1
            if windowFreq[s[r]] == tFreq[s[r]]:
                matches += 1
            print(matches, windowFreq, tFreq)
            while matches == unique:
                if res == "" or len(res) > r - l + 1:
                    res = s[l : r + 1]
                if windowFreq[s[l]] == tFreq[s[l]]:
                    matches -= 1
                windowFreq[s[l]] -= 1
                l += 1
        return res