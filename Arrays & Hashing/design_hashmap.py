"""
https://leetcode.com/problems/design-hashmap/description/
"""

class MyIntialHashMap: #Time complexity O(1), Space complexity O(1)

    def __init__(self):
        self.hashMap = ([None] * 10 ** 6) + [None]
        

    def put(self, key: int, value: int) -> None:
        self.hashMap[key] = value
        

    def get(self, key: int) -> int:
        return self.hashMap[key] if self.hashMap[key] != None else -1
        

    def remove(self, key: int) -> None:
        self.hashMap[key] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
        

#Probably the most comprehensive solution
class ListNode(): #Time complexity O(n), Space complexity O(n)

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hashMap = [ListNode(None, -1) for i in range(1000)]
        

    def put(self, key: int, value: int) -> None:
        cur = self.hashMap[key % 1000]
        while cur.next and cur.next.key != key:
            cur = cur.next

        if not cur.next: 
            cur.next = ListNode(key, value)
        else:
            cur.next.val = value

    def get(self, key: int) -> int:
        cur = self.hashMap[key % 1000]
        while cur.next and cur.next.key != key:
            cur = cur.next

        return cur.next.val if cur.next else -1
        

    def remove(self, key: int) -> None:
        cur = self.hashMap[key % 1000]
        while cur.next and cur.next.key != key:
            cur = cur.next

        if cur.next: cur.next = cur.next.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)