"""
https://leetcode.com/problems/design-browser-history/description/
"""
class Node:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.prev = prev
        self.next = next

#Time complexity O(n), Space complexity O(n)
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.curr = self.head
        
    
    def visit(self, url: str) -> None:
        self.curr.next = Node(url, None, self.curr)
        self.curr = self.curr.next

        
    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1

        return self.curr.val

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1

        return self.curr.val


#Better Alternative
#Time complexity O(1), Space complexity O(n)
class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.pointer = 0
        

    def visit(self, url: str) -> None:
        self.stack = self.stack[:self.pointer+1]
        self.stack.append(url)
        self.pointer += 1

        
    def back(self, steps: int) -> str:
        self.pointer = max(self.pointer - steps, 0)
        return self.stack[self.pointer]

    def forward(self, steps: int) -> str:
        self.pointer = min(self.pointer + steps, len(self.stack)-1)
        return self.stack[self.pointer]
        
