class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append([timestamp, value])
        else:
            self.store[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            l = 0
            r = len(self.store[key]) - 1
            if self.store[key][l][0] > timestamp:
                return ""
            while l < r:
                m = (l + r)//2
                if self.store[key][m][0] > timestamp:
                    r = m - 1
                else:
                    l = m + 1
            if self.store[key][l][0] <= timestamp:
                return self.store[key][l][1]
            else:
                return self.store[key][l - 1][1]
        return ""