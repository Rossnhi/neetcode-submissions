import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        noSpaceStr = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        for i in range(len(noSpaceStr)):
            if noSpaceStr[i] != noSpaceStr[-1 - i]:
                return False
        return True