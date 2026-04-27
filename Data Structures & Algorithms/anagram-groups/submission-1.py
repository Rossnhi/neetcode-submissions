class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabetToNum = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
        anagramHash = {}
        for word in strs:
            wordFreq = [0 for i in range(26)] #
            for letter in word:
                wordFreq[alphabetToNum[letter]] += 1
            if str(wordFreq) in anagramHash:
                anagramHash[str(wordFreq)].append(word);
            else:
                anagramHash[str(wordFreq)] = [word]
        out = []
        for key in anagramHash:
            out.append(anagramHash[key])
        return out