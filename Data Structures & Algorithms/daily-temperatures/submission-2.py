class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)):
            while len(stack) != 0 and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                result[j] = i - j
            stack.append(i)
        return result