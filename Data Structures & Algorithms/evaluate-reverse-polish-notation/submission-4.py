class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calcStack = []
        operators = {"+" : lambda x, y: x + y, "-" : lambda y, x: x - y, "*" : lambda x, y : x * y, "/" : lambda y, x : int(x / y)}
        for token in tokens:
            if token in operators:
                print(calcStack[-1], token, calcStack[-2])
                calcStack.append(operators[token](calcStack.pop(),calcStack.pop()))
                print(calcStack)
            else:
                calcStack.append(int(token))
                print(calcStack)
        return calcStack[0]
            