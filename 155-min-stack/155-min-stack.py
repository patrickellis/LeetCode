class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []
        

    def push(self, val: int) -> None:
        self.min = min(self.min, val)
        if not len(self.stack):
            self.min = val
        self.stack.append((val,self.min))
        print(f'{self.stack[-1][0]} {self.stack[-1][1]}')

    def pop(self) -> None:
        if len(self.stack) > 1:
            self.min = self.stack[-2][1]
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()