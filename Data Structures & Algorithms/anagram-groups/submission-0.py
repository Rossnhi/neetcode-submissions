class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabetToNum = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
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