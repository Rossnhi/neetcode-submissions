import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub( '[^A-Za-z0-9]', '', s).lower()
        for i in range(len(s)):
            if s[i] != s[-i - 1]:
                return False
        return True