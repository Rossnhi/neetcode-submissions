class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        thermometer = {t : [] for t in range(1, 101)}
        result = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)):
            for temp in thermometer:
                if temp > temperatures[i]:
                    thermometer[temp].append(i)
            for temp in thermometer[temperatures[i]]:
                if result[temp] == 0:
                    result[temp] = i - temp
        return result