"""
https://leetcode.com/problems/longest-absolute-file-path/description/
"""

class Solution: #Time complexity O(n^2), Space complexity O(n)
    def lengthLongestPath(self, input: str) -> int:
        paths = input.split("\n") #we get all the sub-path at each level
        stack = []#we append tuples - (total length of the name of files/dir from the root, depth/number of tabs to reach this path)
        res = 0

        for path in paths:
            p = path.split("\t") #\t tells us the depth of the path
            tabs = len(p) - 1 #the num of tabs needed to get to the path
            name = p[-1] #the name of the directory or file
            namelen = len(p[-1]) #the length of the name

            while stack and stack[-1][1] >= tabs: #based on how the hierachy is structured, we can pop paths that are too deep to consider shallow paths, 
		stack.pop()		          #for each path that's added to the stack, we compare to the deepest if it's a file
                

            if not stack:
                stack.append((namelen, tabs)) #if stack is empty, it means we are back to the root directory
            else:
                stack.append((namelen + stack[-1][0], tabs)) #else we update the total length of names as we append to stack

            if "." in name: #this means it's a file
                res = max(res, stack[-1][0] + stack[-1][1]) #add the total length of names to the number of tabs of the deepest file, gives us total length of the paths, number of tabs tells us number of "/" needed

        return res
        