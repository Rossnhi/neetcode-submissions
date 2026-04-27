class Solution:
    def isValid(self, s: str) -> bool:
        nextBracket = []
        openBrackets = {"(" : ")", "[" : "]", "{" : "}"}
        closedBrackets = { ")", "]", "}"}
        for letter in s:
            if letter in openBrackets:
                nextBracket.append(openBrackets[letter])
            elif letter in closedBrackets:
                if len(nextBracket) == 0:
                    return False
                if nextBracket[-1] == letter:
                    nextBracket.pop()
                else:
                    return False
        if len(nextBracket) == 0:
            return True
        return False