class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sKey = [0 for _ in range(26)]
        tKey = [0 for _ in range(26)]
        alphaDict = {chr(i): i - 97 for i in range(ord('a'), ord('z') + 1)}
        for letter in s:
            sKey[alphaDict[letter]] += 1
        for letter in t:
            tKey[alphaDict[letter]] += 1
        if sKey == tKey:
            return True
        return False