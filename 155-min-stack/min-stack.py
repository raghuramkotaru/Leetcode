class MinStack:
    def __init__(self):
        self.s = []
        self.mi = []

    def push(self, val: int) -> None:
        self.s.append(val)
    
        if not self.mi:

            self.mi.append(val)

        else:

            self.mi.append(min(val, self.mi[-1]))

    def pop(self) -> None:
        x = self.s.pop()
        self.mi.pop()
        
        
        return x
    def top(self) -> int:
        
        return self.s[-1]
    def getMin(self) -> int:
        return self.mi[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()