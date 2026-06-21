class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqDict = defaultdict(lambda : [])
        for word in strs:
            freqWord = [0] * 26
            for s in word:
                freqWord[ord(s) - 97] += 1
            key = str(freqWord)
            freqDict[key].append(word)
        res = []
        for key in freqDict:
            res.append(freqDict[key])
        return res