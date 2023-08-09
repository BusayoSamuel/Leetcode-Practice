"""
https://leetcode.com/problems/implement-stack-using-queues/description/
"""
from collections import deque

class MyStack:

    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.popleft())

        res = self.stack1.popleft()

        while self.stack2:
            self.stack1.append(self.stack2.popleft())

        return res
        

    def top(self) -> int:
        while self.stack1:
            if len(self.stack1) == 1:
                res = self.stack1.popleft()
                self.stack2.append(res)
            else:
                self.stack2.append(self.stack1.popleft())

        while self.stack2:
            self.stack1.append(self.stack2.popleft())

        return res
        

    def empty(self) -> bool:
        return len(self.stack1) == 0
    

class MyStack: #Cleaner Version

    def __init__(self):
        self.q = deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q)-1):
            self.push(self.q.popleft())
        return self.q.popleft()
        

    def top(self) -> int:
        return self.q[-1]
        

    def empty(self) -> bool:
        return len(self.q) == 0