"""
https://leetcode.com/problems/design-linked-list/description/
"""

class MyLinkedList1: #Using a singly linked list

    def __init__(self):
        self.val = -1
        self.next = None
        

    def get(self, index: int) -> int:
        if index == 0:
            return self.val
        curr = self.next
        while curr:
            index -= 1
            if not index:
                return curr.val
            curr = curr.next
        return -1 
        

    def addAtHead(self, val: int) -> None:
        if self.val == -1:
            self.val = val
        else:
            temp = MyLinkedList()
            temp.val = self.val
            temp.next = self.next
            self.val = val
            self.next = temp
        

        

    def addAtTail(self, val: int) -> None:
        if self.val == -1:
            self.val = val
        else:
            curr = self

            while curr.next:
                curr = curr.next
        
            tail = MyLinkedList()
            tail.val = val
            tail.next = None
            curr.next = tail
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            curr = self
            while curr:
                index -= 1
                if not index:
                    temp = curr.next
                    insert = MyLinkedList()
                    insert.val = val
                    insert.next = temp
                    curr.next = insert
                    return
                curr = curr.next
            
        

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.next:
                self.val = self.next.val 
                self.next = self.next.next
            else:
                self.val = -1
                print(self)
        else:
            curr = self
            while curr:
                index -= 1
                if not index:
                    curr.next = curr.next.next if curr.next else None
                    return
                curr = curr.next

#Solution 2 - using a doubly linked list plus right and left dummy nodes
class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        node, prev, next = ListNode(val), self.left, self.left.next
        node.next, node.prev = next, prev
        next.prev = node
        prev.next = node

    def addAtTail(self, val: int) -> None:
        node, prev, next = ListNode(val), self.right.prev, self.right
        node.next, node.prev = next, prev
        next.prev = node
        prev.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        next = self.left.next
        while next and index > 0:
            next = next.next
            index -= 1
        
        if next and index == 0:
            node, prev = ListNode(val), next.prev
            node.next, node.prev = next, prev
            next.prev = node
            prev.next = node


    def deleteAtIndex(self, index: int) -> None:
        node = self.left.next
        while node and index > 0:
            node = node.next
            index -= 1
        
        if node and node != self.right and index == 0:
            node.prev.next = node.next
            node.next.prev = node.prev




