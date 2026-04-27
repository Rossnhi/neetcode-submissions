class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tDict = {}
        sDict = {}
        for letter in t:
            if letter in tDict:
                tDict[letter] += 1
            else:
                tDict[letter] = 1
        for letter in s:
            if letter in sDict:
                sDict[letter] += 1
            else:
                sDict[letter] = 1
        for letter in sDict:
            if letter not in tDict:
                return False
            if sDict[letter] != tDict[letter]:
                return False
        for letter in tDict:
            if letter not in sDict:
                return False
        return True