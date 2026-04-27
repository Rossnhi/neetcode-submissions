class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append([timestamp, value])
        else:
            self.map[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        if key not in self.map:
            return ""
        r = len(self.map[key]) - 1
        if self.map[key][0][0] > timestamp:
            return ""
        while l < r:
            m = (l + r)//2
            if self.map[key][m][0] > timestamp:
                r = m - 1
            else:
                l = m + 1
        if self.map[key][l][0] <= timestamp:
            return self.map[key][l][1]
        return self.map[key][l - 1][1]