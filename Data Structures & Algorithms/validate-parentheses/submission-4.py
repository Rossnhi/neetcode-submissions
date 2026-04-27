class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"(" : ")", "{" : "}", "[" : "]"}
        closed = {")", "}", "]"}
        for c in s:
            print(c, stack)
            if c in brackets:
                stack.append(c)
            if c in closed:
                if len(stack) == 0:
                    return False
                if brackets[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False