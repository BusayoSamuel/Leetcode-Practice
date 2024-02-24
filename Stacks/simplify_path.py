"""
https://leetcode.com/problems/simplify-path/description/
"""

class Solution: #Time complexity O(n), Space complexity O(n)
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = ""

        for c in path:
            if c != "/":
                curr += c
            else:
                if curr == "..":
                    if stack: stack.pop()
                elif curr != "" and curr != ".":
                    stack.append(curr)
                curr = ""

        return "/" + "/".join(stack)

class AlternativeSolution: #Different Structure, Same complexity
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""
        r = 0

        while r < len(path):
            while r < len(path) and path[r] != "/" :
                cur += path[r]
                r += 1

            if cur == "." or cur == "":
                pass
            elif cur == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(cur)
            
            cur = ""
            r += 1 

        return "/" + "/".join(stack) 
            

        
