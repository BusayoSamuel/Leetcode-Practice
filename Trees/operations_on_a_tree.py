"""
https://leetcode.com/problems/operations-on-tree/description/
"""
class LockingTree: 

    def __init__(self, parent: List[int]): #Time complexity O(n), Space complexity O(n)
        self.tree = {}
        for node, par in enumerate(parent):
            if par in self.tree:
                self.tree[par]['children'].append(node)
            else:
                self.tree[par] = {'parent': None, 'children': [node], 'locked': [False]}

            if node in self.tree:
                self.tree[node]['parent'] = par
            else:
                self.tree[node] = {'parent': par, 'children': [], 'locked': [False]}

        

    def lock(self, num: int, user: int) -> bool: #Time complexity O(1), Space complexity O(1)
        if self.tree[num]['locked'][0]:
            return False
        else:
            self.tree[num]['locked'] = [True, user]
            return True
        

    def unlock(self, num: int, user: int) -> bool: #Time complexity O(1), Space complexity O(1)
        if self.tree[num]['locked'][0] and self.tree[num]['locked'][1] == user:
            self.tree[num]['locked'] = [False]
            return True
        else:
            return False

    def upgrade(self, num: int, user: int) -> bool: #Time complexity O(n), Space complexity O(1)
        if self.tree[num]['locked'][0]:
            return False
        
        q = deque(self.tree[num]['children'])
        found = False
        while q:#no need for an inner loop, as this would pass through each level anyway
            node = q.popleft()
    
            if self.tree[node]['locked'][0]:
                found = True
                if found:
                    break
    
            q.extend(self.tree[node]['children'])
            
            if found:
                break

        if not found:
            return False

        cur = num
        while cur != -1:
            cur = self.tree[cur]['parent']
            if self.tree[cur]['locked'][0]:
                return False
            
            

        self.tree[num]['locked'] = [True, user]
        q = deque(self.tree[num]['children'])
        while q:#no need for an inner loop, as this would pass through each level anyway
            node = q.popleft() 

            self.tree[node]['locked'] = [False]

            q.extend(self.tree[node]['children'])

        return True
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)


##Alternatively
from collections import deque
from typing import List

class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.children = {i: [] for i in range(len(parent))}
        self.locked = {i: (False, None) for i in range(len(parent))}
        
        for child, par in enumerate(parent):
            if par != -1:  # Ignore the root since it has no parent
                self.children[par].append(child)
    
    def lock(self, num: int, user: int) -> bool:
        if self.locked[num][0]:
            return False
        self.locked[num] = (True, user)
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num][0] and self.locked[num][1] == user:
            self.locked[num] = (False, None)
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        if self.locked[num][0]:
            return False

        # Check if any ancestor is locked
        cur = num
        while cur != -1:
            if self.locked[cur][0]:
                return False
            cur = self.parent[cur]

        # Check if any descendant is locked
        found_locked_descendant = False
        q = deque([num])
        
        while q:
            node = q.popleft()
            if self.locked[node][0]:
                found_locked_descendant = True
                break
            q.extend(self.children[node])
        
        if not found_locked_descendant:
            return False

        # Unlock all descendants
        q = deque([num])
        while q:
            node = q.popleft()
            if self.locked[node][0]:
                self.locked[node] = (False, None)
            q.extend(self.children[node])

        # Lock the current node
        self.locked[num] = (True, user)
        return True

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
