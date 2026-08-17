import bisect
class Value:
    def __init__(self, value: str, timestamp: int) -> None:
        self.value = value
        self.timestamp = timestamp

class TimeMap:

    def __init__(self):
        self.key_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_map:
            self.key_map[key] = []
        self.key_map[key].append(Value(value=value, timestamp=timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_map:
            return ""
        idx = bisect.bisect_right(self.key_map[key], timestamp, key=lambda a: a.timestamp)
        if idx == 0:
            return ""
        return self.key_map[key][idx-1].value
