class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freqS1 = defaultdict(int)
        unique = 0
        for s in s1:
            freqS1[s] += 1
            if freqS1[s] == 1:
                unique += 1
        matches = 0
        freqWindow = defaultdict(int)
        for i in range(len(s1)):
            freqWindow[s2[i]] += 1
            if freqS1[s2[i]] == freqWindow[s2[i]]:
                matches += 1
        if matches == unique:
            return True
        for l in range(len(s2) - len(s1)):
            r = l + len(s1)
            freqWindow[s2[r]] += 1
            if freqS1[s2[r]] == freqWindow[s2[r]]:
                matches += 1
            freqWindow[s2[l]] -= 1
            if freqS1[s2[l]] - freqWindow[s2[l]] == 1:
                matches -= 1
            print(s2[l], s2[r], matches)
            if matches == unique:
                return True
        return False