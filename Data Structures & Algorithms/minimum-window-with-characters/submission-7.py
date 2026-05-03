class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sWindowDict = defaultdict(lambda : 0)
        tDict = defaultdict(lambda : 0)
        matchTarget = 0
        for ch in t:
            if ch in tDict: 
                tDict[ch] = tDict[ch] + 1 
            else:
                tDict[ch] = 1
                matchTarget += 1
        res = ""
        matches = 0
        l = 0
        for r in range(len(s)):
            if tDict[s[r]] - sWindowDict[s[r]] == 1:
                matches += 1
            print(r, matches)
            sWindowDict[s[r]] = sWindowDict[s[r]] + 1 if s[r] in sWindowDict else 1
            if matches == matchTarget:
                while True:
                    res = s[l : r + 1] if res == "" or len(res) > r - l + 1 else res
                    if tDict[s[l]] - sWindowDict[s[l]] == 0:
                        matches -= 1
                        sWindowDict[s[l]] -= 1
                        l += 1
                        break;
                    sWindowDict[s[l]] -= 1
                    l += 1
        return res  