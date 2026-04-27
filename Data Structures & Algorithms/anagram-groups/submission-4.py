class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        alphaToNum = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7, 'i' : 8, 'j' : 9, 'k' : 10, 'l' : 11, 'm' : 12, 'n' : 13, 'o' : 14, 'p' : 15, 'q' : 16, 'r' : 17, 's' : 18, 't' : 19, 'u' : 20, 'v' : 21, 'w' : 22, 'x' : 23, 'y' : 24, 'z' : 25}
        for word in strs:
            key = [0 for _ in range(26)]
            for letter in word:
                key[alphaToNum[letter]] += 1
            if str(key) in anagrams:
                anagrams[str(key)].append(word)
            else:
                anagrams[str(key)] = [word]
        out = []
        for word in anagrams:
            out.append(anagrams[word])
        return out