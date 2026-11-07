import bisect
class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # sorted insertion
        idx = bisect.bisect_right(self.map[key], timestamp, key = lambda item: item[0])
        if idx == 0:
            self.map[key].insert(idx,(timestamp, value))
        elif idx == len(self.map[key]):
            self.map[key].append((timestamp, value))
        else:
            self.map[key].insert(idx,(timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if len(self.map[key]) == 0:
            return ""
        idx = bisect.bisect_right(self.map[key], timestamp, key = lambda item: item[0])
        if idx == 0:
            return ""
        timestamp_prev, val_prev = self.map[key][idx - 1]
        return val_prev
