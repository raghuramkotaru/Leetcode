class MedianFinder:

    def __init__(self):
        
        self.h = []
        

    def addNum(self, num: int) -> None:
        
       self.h.append(num)
    def findMedian(self) -> float:
        self.h.sort()
        n = len(self.h)
        if n%2 == 0:
            return (((self.h[n//2])+(self.h[n//2-1]))/2)
        else:
            return (self.h[n//2])




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()