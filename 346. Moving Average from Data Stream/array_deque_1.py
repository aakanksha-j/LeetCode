class MovingAverage:
    # using deque
    # time O(1)
    # space O(N)
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.queue_sum = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        tail = self.queue.popleft() if len(self.queue) > self.size else 0
        self.queue_sum += val - tail
        return self.queue_sum / min(len(self.queue), self.size)
            


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

    # using array
    # time O(N)
    # space O(N)
    def __init__(self, size: int):
        self.size = size
        self.array = []

    def next(self, val: int) -> float:
        if len(self.array) < self.size:
            self.array.append(val)
            return sum(self.array)/len(self.array)
            
        else:
            self.array.pop(0)
            self.array.append(val)
            return sum(self.array)/self.size