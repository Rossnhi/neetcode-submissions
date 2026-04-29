class Solution:
    def minWindow(self, s: str, t: str) -> str:
        alpha = {chr(_) : _ - 65 for _ in range(65, 123)}
        uniqCharsT = 0
        freqT = [0 for _ in range(58)]
        for c in t:
            if freqT[alpha[c]] == 0:
                uniqCharsT += 1
            freqT[alpha[c]] += 1
        freqWindow = [0 for _ in range(58)]
        res = ""
        matches = 0
        l = 0
        for r in range(len(s)):
            if freqT[alpha[s[r]]] - freqWindow[alpha[s[r]]] == 1:
                matches += 1
            print(s[r], matches)
            freqWindow[alpha[s[r]]] += 1
            while matches == uniqCharsT:
                res = s[l: r + 1] if len(res) > r - l + 1 or res == "" else res
                if freqT[alpha[s[l]]] - freqWindow[alpha[s[l]]] == 0:
                    matches -= 1
                freqWindow[alpha[s[l]]] -= 1
                l += 1
        return res







