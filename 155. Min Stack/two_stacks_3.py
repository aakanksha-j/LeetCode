class MinStack:
    """Runtime: 60 ms
       Memory: 18 MB"""

    def __init__(self):
        """
        Use two stacks, one of value, other of min_value.
        """
        self.stack = []
        self.min_tracker_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_tracker_stack or x <= self.min_tracker_stack[-1]:
            self.min_tracker_stack.append(x)

    def pop(self) -> None:
        if self.stack[-1] == self.min_tracker_stack[-1]:
            self.min_tracker_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_tracker_stack[-1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.pop()
param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()
print(param_4)
