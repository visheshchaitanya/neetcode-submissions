class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        val_list = self.time_map.get(key)
        if val_list is None:
            return ""
        
        start = 0
        end = len(val_list) - 1
        ans = -1

        while start <= end:
            mid = start + (end - start) // 2
            if val_list[mid][0] <= timestamp:
                ans = mid
                start = mid + 1
            else:
                end = mid - 1
        
        return "" if ans == -1 else val_list[ans][1]
        
