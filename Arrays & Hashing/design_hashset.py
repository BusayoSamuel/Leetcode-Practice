"""
https://leetcode.com/problems/design-hashset/description/
"""

class MyHashSet: #Inefficient style, Time complexity O(n) due to append function, Space complexity O(n)

    def __init__(self):
        self.arr = [] #1D array
        

    def add(self, key: int) -> None:
        if key in self.arr:
            return
        else:
            self.arr.append(key)
            
    def remove(self, key: int) -> None:
        for idx in range(len(self.arr)):
            if self.arr[idx] == key:
                del self.arr[idx]
                return
        

    def contains(self, key: int) -> bool:
        if key in self.arr:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
        
class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet: #Efficient solution, Time complexity is either O(1) or O(n) depending on the input, Space complexity O(n)
    
    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)]
        

    def add(self, key: int) -> None:
        cur = self.set[key%10**4]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)
        

    def remove(self, key: int) -> None:
        cur = self.set[key%10**4]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        

    def contains(self, key: int) -> bool:
        cur = self.set[key%10**4]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)