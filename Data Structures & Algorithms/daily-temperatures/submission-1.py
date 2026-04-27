class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        temp = []
        for i in range(len(temperatures)):
            while temp and temperatures[temp[-1]] < temperatures[i]:
                j = temp.pop()
                result[j] = i - j
            temp.append(i)
        return result