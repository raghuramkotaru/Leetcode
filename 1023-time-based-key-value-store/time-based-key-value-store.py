class TimeMap:

    def __init__(self):
        self.h = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.h:
            self.h[key] = []
        self.h[key].append([value,timestamp])
    def get(self, key: str, timestamp: int) -> str:

        res =""
        if key in self.h:
            val = self.h[key]
            l,r = 0, len(val)-1
            while l<=r:
                m = (l+r)//2
                if val[m][1] <= timestamp:
                    res = val[m][0]
                    l = m+1
                else:
                    r = m-1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)