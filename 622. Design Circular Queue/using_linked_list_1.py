class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.head = None
        self.tail = None
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.count == self.capacity:
            return False
        newNode = ListNode(value)
        if self.count == 0:
            self.head = newNode
            self.tail = newNode
            self.head.next = self.tail
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.head = self.head.next
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return True if self.count == 0 else False

    def isFull(self) -> bool:
        return True if self.count == self.capacity else False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
