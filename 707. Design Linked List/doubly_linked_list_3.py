# https://leetcode.com/problems/design-linked-list/discuss/702777/Java-Solution-using-Doubly-LinkedList-7-ms-faster-than-96.65

# passed next and prev values for node in Node declaration
# add at head and tail are written separately from add at index

class Node:

    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        if not self.head:
            return -1

        curr = self.head
        for _ in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.head, None)
        #node.next = self.head

        if not self.head:
            self.head = node
            self.tail = node

        else:
            self.head.prev = node
            self.head = node

        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val, None, self.tail)

        if not self.tail:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        elif index == self.size:
            self.addAtTail(val)
            return

        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            node = Node(val, curr.next, curr)

            curr.next.prev = node
            curr.next = node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

        elif index == self.size - 1:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None

        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            curr.next.prev = curr.prev
            curr.prev.next = curr.next

        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
