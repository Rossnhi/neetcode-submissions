class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sKey = [0 for _ in range(26)]
        tKey = [0 for _ in range(26)]
        alphaDict = {chr(i + 97) : i for i in range(26)}
        for c in s:
            sKey[alphaDict[c]] += 1
        for c in t:
            tKey[alphaDict[c]] += 1
        return sKey == tKey