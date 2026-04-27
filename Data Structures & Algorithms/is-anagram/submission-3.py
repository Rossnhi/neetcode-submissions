class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sKey = [0 for _ in range(26)]
        tKey = [0 for _ in range(26)]
        alphabetToNum = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7, 'i' : 8, 'j' : 9, 'k' : 10, 'l' : 11, 'm' : 12, 'n' : 13, 'o' : 14, 'p' : 15, 'q' : 16, 'r' : 17, 's' : 18, 't' : 19, 'u' : 20, 'v' : 21, 'w' : 22, 'x' : 23, 'y' : 24, 'z' : 25}
        for letter in s:
            sKey[alphabetToNum[letter]] += 1
        for letter in t:
            tKey[alphabetToNum[letter]] += 1
        if sKey == tKey:
            return True
        return False