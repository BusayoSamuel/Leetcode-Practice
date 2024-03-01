"""
https://leetcode.com/problems/design-circular-queue/description/
"""

class MyListNode:

    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = ListNode()
        curr = self.head
        for i in range(k-1):
            node = ListNode()
            curr.next = node
            curr = curr.next
        curr.next = self.head
        self.tail = self.head

    def enQueue(self, value: int) -> bool:

        if self.isFull(): return False
        
        if not self.isEmpty():
            self.tail = self.tail.next

        self.tail.val = value

        return True
                
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        curr = self.head
        tmp = curr.next
        curr.val = None
        if self.tail == self.head:
            self.tail = tmp
        self.head = tmp

        return True

    def Front(self) -> int:
        if self.head.val == None:
            return -1
        else:
            return self.head.val
        

    def Rear(self) -> int:
        if self.tail.val == None:
            return -1
        else:
            return self.tail.val

    def isEmpty(self) -> bool:
        return self.head.val == None

    def isFull(self) -> bool:
        return self.tail.val != None and self.tail.next == self.head
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


##Alternatively
class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class MyCircularQueue:

    def __init__(self, k: int):
        self.head = self.tail = None
        self.capacity = k
        self.size = 0


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        node = Node(value)
        if self.size == 0:
            self.head = self.tail = node
        else:
            self.tail.next = self.tail = node

        self.size += 1

        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.head = self.head.next
        self.size -= 1

        return True


    def Front(self) -> int:
        return -1 if self.isEmpty() else self.head.val


    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.tail.val


    def isEmpty(self) -> bool:
        return self.size == 0


    def isFull(self) -> bool:
        return self.capacity == self.size


