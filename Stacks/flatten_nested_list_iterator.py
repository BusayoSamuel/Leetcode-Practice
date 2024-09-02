"""
https://leetcode.com/problems/flatten-nested-list-iterator/description/
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> [NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self.dfs(nestedList)
        self.stack.reverse()
        
    
    def next(self) -> int:
        return self.stack.pop()
    
    def hasNext(self) -> bool:
        return True if self.stack else False

    def dfs(self, nestedList):
        for item in nestedList:
            if item.isInteger():
                self.stack.append(item.getInteger())
            else:
                self.dfs(item.getList()) 
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
