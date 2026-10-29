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
            for time, val in self.KVStore[key]:
                if time <= timestamp:
                    value = val
                else:
                    break
        return value