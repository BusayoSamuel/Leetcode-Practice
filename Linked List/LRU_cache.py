"""
https://leetcode.com/problems/lru-cache/description/
"""

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache: #Optimal solution, Time complexity O(1), Space complexity O(capacity)
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.right, self.left = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        prev, right = self.right.prev, self.right
        prev.next = node
        right.prev = node
        node.prev = prev
        node.next = self.right

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1  
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

#My Solution
class Node:
    def __init__(self, key = None, val = None, prev = None, next = None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap = {}
        

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            res = node.val
            prevNode = node.prev
            nextNode = node.next
            temp = node
            prevNode.next = nextNode
            nextNode.prev = prevNode
            prevNode = self.tail.prev
            prevNode.next = temp
            temp.prev = prevNode
            temp.next = self.tail
            self.tail.prev = temp
            return res
        else:
            return -1      

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            prevNode = node.prev
            nextNode = node.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev.next = node
            self.tail.prev = node
        else:
            node = Node(key, value, self.tail.prev, self.tail)
            self.tail.prev.next = node
            self.tail.prev = node
            self.hashmap[key] = node

            if not self.cap:
                delkey = self.head.next.key
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                del self.hashmap[delkey]
            else:
                self.cap -= 1
