"""
https://leetcode.com/problems/implement-queue-using-stacks/description/
"""

class MyQueue: #My Solution, Time complexity O(n), Space complexity 0(n) 

    def __init__(self):
        self.tailStack = []
        self.headStack = []
        

    def push(self, x: int) -> None:
        self.tailStack.append(x)
        

    def pop(self) -> int:
        while self.tailStack:
            self.headStack.append(self.tailStack.pop())

        res = self.headStack.pop()

        while self.headStack:
            self.tailStack.append(self.headStack.pop())

        return res

    def peek(self) -> int:
        while self.tailStack:
            self.headStack.append(self.tailStack.pop())

        res = self.headStack[-1]

        while self.headStack:
            self.tailStack.append(self.headStack.pop())

        return res
        

    def empty(self) -> bool:
        return not self.tailStack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


class MyQueue: #Same complexity as above, but the amortized/average time complexity would be O(n)

    def __init__(self):
        self.tailStack = []
        self.headStack = []
        

    def push(self, x: int) -> None:
        self.tailStack.append(x)
        

    def pop(self) -> int:
        if not self.headStack: #This O(n) case wouldn't always happen
            while self.tailStack:
                self.headStack.append(self.tailStack.pop())
        return self.headStack.pop()

    def peek(self) -> int:
        if not self.headStack: #This O(n) case wouldn't always happen
            while self.tailStack:
                self.headStack.append(self.tailStack.pop())
        return self.headStack[-1]
        
    def empty(self) -> bool:
        return not self.tailStack and not self.headStack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
