class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        unique = 0
        freqS1 = defaultdict(int)
        for i in range(len(s1)):
            freqS1[s1[i]] += 1
            if freqS1[s1[i]] == 1:
                unique += 1
        windowFreq = defaultdict(int)
        matches = 0
        for i in range(len(s1)):
            if freqS1[s2[i]] - windowFreq[s2[i]] == 1:
                matches += 1
            windowFreq[s2[i]] += 1
        if matches == unique:
            return True
        for l in range(len(s2) - len(s1)):
            if freqS1[s2[l]] - windowFreq[s2[l]] == 0:
                matches -= 1
            windowFreq[s2[l]] -= 1
            r = l + len(s1)
            if freqS1[s2[r]] - windowFreq[s2[r]] == 1:
                matches += 1
            windowFreq[s2[r]] += 1
            if matches == unique:
                return True
        return False