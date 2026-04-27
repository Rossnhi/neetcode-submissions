class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '+' : lambda y, x : x + y,
            '-' : lambda y, x : x - y,
            '*' : lambda y, x : x * y,
            '/' : lambda y, x : int(x / y),
        }
        for token in tokens:
            print(stack)
            if token not in operators:
                stack.append(int(token))
            else:
                stack.append(operators[token](stack.pop(), stack.pop()))
        return stack[0]