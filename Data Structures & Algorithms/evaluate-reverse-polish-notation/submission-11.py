class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+" : lambda  y, x : x + y,
            "-" : lambda  y, x : x - y,
            "*" : lambda  y, x : x * y,
            "/" : lambda  y, x : int(x / y)
            }
        callStack = []
        for token in tokens:
            print(callStack)
            if token in operators:
                callStack.append(operators[token](callStack.pop(), callStack.pop()))
            else:
                callStack.append(int(token))
        return callStack.pop()