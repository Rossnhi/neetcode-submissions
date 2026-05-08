class Solution:
    def isValid(self, s: str) -> bool:
        brackets = set(["(", "[", "{"])
        bracketPartner = {
            "}" : "{",
            "]" :"[",
            ")" : "("
        }
        bracketStack = []
        for b in s:
            if b in brackets:
                bracketStack.append(b)
            elif b in bracketPartner:
                if len(bracketStack) == 0:
                    return False
                if bracketPartner[b] == bracketStack[-1]:
                    bracketStack.pop()
                else:
                     return False
        if len(bracketStack) != 0:
            return False
        return True