class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calcStack = []
        operators = {"+" : lambda y, x: x + y, "-" : lambda y, x: x - y, "*" : lambda y, x : x * y, "/" : lambda y, x : int(x / y)}
        for token in tokens:
            if token in operators:
                calcStack.append(operators[token](calcStack.pop(),calcStack.pop()))
            else:
                calcStack.append(int(token))
        return calcStack[0]
            