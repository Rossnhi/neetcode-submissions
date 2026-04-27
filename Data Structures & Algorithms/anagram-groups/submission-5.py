class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        alphaDict = {chr(i + 97) : i for i in range(26)}
        for word in strs:
            key = [0 for _ in range(26)]
            for letter in word:
                key[alphaDict[letter]] += 1
            if str(key) in anagrams:
                anagrams[str(key)].append(word)
            else:
                anagrams[str(key)] = [word]
        out = []
        for group in anagrams:
            out.append(anagrams[group])
        return out