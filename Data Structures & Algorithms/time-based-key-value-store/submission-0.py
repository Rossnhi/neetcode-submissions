class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append([timestamp, value])
        else:
            self.data[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.data:
            l = 0
            r = len(self.data[key]) - 1
            while l <= r:
                mid = l + int((r - l)/2)
                if self.data[key][mid][0] <= timestamp:
                    l = mid + 1
                else:
                    r = mid - 1
            if self.data[key][l - 1][0] <= timestamp:
                return self.data[key][l - 1][1]
            else:
                return ""
        else:
            return ""