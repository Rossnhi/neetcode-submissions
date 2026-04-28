class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        alpha = {chr(_) : _ - 97 for _ in range(97, 123)}
        freqS1 = [0 for _ in range(26)]
        freq = [0 for _ in range(26)]
        for c in range(len(s1)):
            freqS1[alpha[s1[c]]] += 1
            freq[alpha[s2[c]]] += 1
        matches = 0
        for _ in range(26):
            if freqS1[_] == freq[_]:
                matches += 1
        if matches == 26:
            return True
        for l in range(1, len(s2) - len(s1) + 1):
            freq[alpha[s2[l - 1]]] -= 1
            if freqS1[alpha[s2[l - 1]]] - freq[alpha[s2[l - 1]]] == 1:
                matches -= 1
            elif freqS1[alpha[s2[l - 1]]] - freq[alpha[s2[l - 1]]] == 0:
                matches += 1
            freq[alpha[s2[l + len(s1) - 1]]] += 1
            if freqS1[alpha[s2[l + len(s1) - 1]]] - freq[alpha[s2[l + len(s1) - 1]]] == -1:
                matches -= 1
            elif freqS1[alpha[s2[l + len(s1) - 1]]] - freq[alpha[s2[l + len(s1) - 1]]] == 0:
                matches += 1
            if matches == 26:
                return True
        return False