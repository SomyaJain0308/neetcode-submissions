class TimeMap:

    def __init__(self):
        self.KVStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.KVStore:
            self.KVStore[key] = []
        self.KVStore[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        value = ""
        if key in self.KVStore:
            pairs = self.KVStore[key]
            l, r = 0, len(pairs) - 1
            while l <= r:
                m = (l + r) // 2
                if pairs[m][0] > timestamp:
                    r = m - 1
                else:
                    l = m + 1
                    value = pairs[m][1]
        return value