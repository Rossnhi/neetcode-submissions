class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freqS1 = defaultdict(int)
        unique = 0
        for ch in s1:
            if freqS1[ch] == 0:
                unique += 1
            freqS1[ch] += 1
        freqS2Window = defaultdict(int)
        matches = 0
        for i in range(len(s1)):
            if freqS1[s2[i]] - freqS2Window[s2[i]] == 1:
                matches += 1
            freqS2Window[s2[i]] += 1
            if matches == unique:
                return True
        for l in range(len(s2) - len(s1)):
            print(s2[l:l + len(s1)], matches, freqS2Window)
            if freqS1[s2[l]] - freqS2Window[s2[l]] == 0:
                matches -= 1
            freqS2Window[s2[l]] -= 1
            if freqS1[s2[l + len(s1)]] - freqS2Window[s2[l + len(s1)]] == 1:
                matches += 1
            freqS2Window[s2[l + len(s1)]] += 1
            if matches == unique:
                return True
        return False